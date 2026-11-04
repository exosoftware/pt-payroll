"""Replace the custom "Assiduidade" work entry type with Odoo's native one.

The module used to define its own attendance work entry type
(``ptplus_payroll.entry_type_pt_attendance``, code ``ASSIDUIDADE``) even though
the native ``hr_work_entry.work_entry_type_attendance`` (code ``WORK100``,
translated "Assiduidade" in pt_PT) serves the same purpose. Repoint every
existing reference to the native type, then delete the custom one.
"""

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

_CUSTOM_XMLID = "ptplus_payroll.entry_type_pt_attendance"
_NATIVE_XMLID = "hr_work_entry.work_entry_type_attendance"

# Tables with a foreign key to hr_work_entry_type that may point at the
# custom attendance type.
_TABLES = [
    ("hr_work_entry", "work_entry_type_id"),
    ("hr_payslip_worked_days", "work_entry_type_id"),
    ("resource_calendar_attendance", "work_entry_type_id"),
    ("resource_calendar_leaves", "work_entry_type_id"),
    ("hr_payroll_structure_type", "default_work_entry_type_id"),
]


@openupgrade.migrate()
def migrate(env, version):
    custom = env.ref(_CUSTOM_XMLID, raise_if_not_found=False)
    if not custom:
        _logger.info("Custom Assiduidade work entry type not found; nothing to do.")
        return
    native = env.ref(_NATIVE_XMLID)

    for table, column in _TABLES:
        env.cr.execute(
            f"UPDATE {table} SET {column} = %s WHERE {column} = %s",
            (native.id, custom.id),
        )
        _logger.info(
            "%s: %s row(s) repointed to the native Attendance work entry type.",
            table,
            env.cr.rowcount,
        )

    # Delete via SQL: hr_payroll blocks hr.work.entry.type unlink at ORM
    # level ("You cannot delete work entry type(s). Instead archive it.").
    # Any reference not listed in _TABLES keeps its foreign key, which blocks
    # this delete and fails the migration loudly instead of losing data.
    env.cr.execute("DELETE FROM hr_work_entry_type WHERE id = %s", (custom.id,))
    env.cr.execute(
        "DELETE FROM ir_model_data WHERE model = 'hr.work.entry.type' AND res_id = %s",
        (custom.id,),
    )
    _logger.info("Custom Assiduidade work entry type deleted.")
