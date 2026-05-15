import logging
from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

@openupgrade.migrate()
def migrate(env, version):
    _logger.info("Migrating l10n_pt_niss to ssnid for employees")

    # Check if ssnid column exists in hr_employee (it should in v17)
    # If this is a pre-migration, ssnid might have been added by the Odoo core update
    # but we want to make sure we don't fail if it's not there yet for some reason.
    # However, ssnid is a standard field in hr.employee in v17.

    # We use SQL for efficiency and to avoid model loading issues during pre-migration

    # 1. Update hr_employee
    if openupgrade.column_exists(env.cr, "hr_employee", "l10n_pt_niss"):
        # Ensure ssnid column exists. In pre-migration, if we are upgrading to 17.0,
        # Odoo might not have created the column yet if it's a new field in core.
        # But ssnid was added in Odoo 17.0 core.
        if not openupgrade.column_exists(env.cr, "hr_employee", "ssnid"):
            _logger.info("Creating ssnid column in hr_employee as it does not exist yet")
            env.cr.execute("ALTER TABLE hr_employee ADD COLUMN ssnid VARCHAR")

        _logger.info("Copying l10n_pt_niss to ssnid in hr_employee")
        env.cr.execute(
            """
            UPDATE hr_employee
            SET ssnid = l10n_pt_niss
            WHERE (ssnid IS NULL OR ssnid = '')
              AND l10n_pt_niss IS NOT NULL
              AND l10n_pt_niss != ''
            """
        )
