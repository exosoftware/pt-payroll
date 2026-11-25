from odoo.tools.sql import column_exists


def migrate(cr, version):
    """
    The employee's own "Non Resident" field is merged into the payroll's
    "Non-resident" of the employee, which the Modelo 30 and the DMR read.
    """
    if not column_exists(cr, "hr_employee", "l10n_pt_non_resident"):
        return
    cr.execute(
        """
        UPDATE hr_employee
        SET is_non_resident = TRUE
        WHERE l10n_pt_non_resident
            AND is_non_resident IS NOT TRUE
        """
    )
