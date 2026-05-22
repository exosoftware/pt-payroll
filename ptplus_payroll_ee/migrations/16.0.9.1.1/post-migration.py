import logging
from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

@openupgrade.migrate()
def migrate(env, version):
    _logger.info("Migrating l10n_pt_vat for employees from address_home_id.vat")
    env.cr.execute(
        """
        UPDATE hr_employee e
        SET l10n_pt_vat = p.vat
        FROM res_partner p
        WHERE e.address_home_id = p.id
          AND (e.l10n_pt_vat IS NULL OR e.l10n_pt_vat = '')
          AND p.vat IS NOT NULL
          AND p.vat != ''
        """
    )
