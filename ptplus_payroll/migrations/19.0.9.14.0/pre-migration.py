from odoo.tools.sql import column_exists


def migrate(cr, version):
    """
    The employee's own "Non Resident" field is merged into the payroll's
    "Non-resident" of the contract, which the Modelo 30 and the DMR read. The
    old field had no date, so every version of the employee is marked.
    """
    if not column_exists(cr, "hr_employee", "l10n_pt_non_resident"):
        return
    cr.execute(
        """
        UPDATE hr_version version
        SET is_non_resident = TRUE
        FROM hr_employee employee
        WHERE employee.id = version.employee_id
            AND employee.l10n_pt_non_resident
            AND version.is_non_resident IS NOT TRUE
        """
    )
