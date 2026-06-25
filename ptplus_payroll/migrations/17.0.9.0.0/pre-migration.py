import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


_COLLIDING_XMLID = "wizard_payroll_statement_form"


def _resolve_collision(env):
    """Drop the redundant _ee primary view that collides with the base view.

    Both ``ptplus_payroll.wizard_payroll_statement_form`` and
    ``ptplus_payroll_ee.wizard_payroll_statement_form`` exist on installs that
    have both modules. After the module rename they would map to the same
    ``(module, name)`` pair in ``ir_model_data``. Redirect references to the
    base view, then remove the redundant one.
    """
    imd = env["ir.model.data"]
    base = imd.search(
        [("module", "=", "ptplus_payroll"), ("name", "=", _COLLIDING_XMLID)],
        limit=1,
    )
    ee = imd.search(
        [("module", "=", "ptplus_payroll_ee"), ("name", "=", _COLLIDING_XMLID)],
        limit=1,
    )
    if not ee:
        return
    if not base:
        # Nothing to merge into — just rename the ee record so it survives.
        ee.write({"module": "ptplus_payroll"})
        return

    base_view_id = base.res_id
    ee_view_id = ee.res_id

    # Redirect actions and inherited views pointing at the ee primary view.
    env.cr.execute(
        "UPDATE ir_act_window SET view_id = %s WHERE view_id = %s",
        (base_view_id, ee_view_id),
    )
    env.cr.execute(
        "UPDATE ir_act_window_view SET view_id = %s WHERE view_id = %s",
        (base_view_id, ee_view_id),
    )
    env.cr.execute(
        "UPDATE ir_ui_view SET inherit_id = %s WHERE inherit_id = %s",
        (base_view_id, ee_view_id),
    )

    # Drop the redundant view and its ir_model_data entry.
    env.cr.execute("DELETE FROM ir_ui_view WHERE id = %s", (ee_view_id,))
    ee.unlink()


@openupgrade.migrate()
def migrate(env, version):
    if not openupgrade.is_module_installed(env.cr, "ptplus_payroll_ee"):
        _logger.info("ptplus_payroll_ee is not installed; skipping merge migration.")
        return

    _logger.info(
        "Merging ptplus_payroll_ee into ptplus_payroll: "
        "redirecting ir_model_data and uninstalling the legacy module."
    )

    _resolve_collision(env)

    # Re-point every remaining XML ID, translation and module dependency from
    # ptplus_payroll_ee to ptplus_payroll. merge_modules=True is the supported
    # flag for absorbing one module into another that already exists.
    openupgrade.update_module_names(
        env.cr,
        [("ptplus_payroll_ee", "ptplus_payroll")],
        merge_modules=True,
    )

    # update_module_names sets state='to remove'. Flush so the module is
    # uninstalled cleanly during this upgrade pass instead of lingering.
    env.cr.execute(
        """
        UPDATE ir_module_module
        SET state = 'uninstalled', latest_version = NULL
        WHERE name = 'ptplus_payroll_ee'
        """
    )
