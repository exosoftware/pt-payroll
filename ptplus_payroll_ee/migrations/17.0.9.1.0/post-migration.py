import logging

from openupgradelib import openupgrade


_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    complements = (
        env["hr.salary.complement.pt"].search([])
    )
    for comp in complements:
        if comp.is_attachment:
            comp.attachment_payslip_ids = comp.payslip_ids
            comp.payslip_ids = False
