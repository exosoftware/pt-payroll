from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env.cr.execute(
        """
        UPDATE hr_payslip p
        SET l10n_pt_independent_slip =
            CASE
                WHEN p.l10n_pt_independent_slip = 'true'
                     AND EXISTS (
                         SELECT 1
                         FROM hr_payslip_line l
                         WHERE l.slip_id = p.id
                           AND l.code = 'SUBS_FER'
                     )
                    THEN 'holidays'
                WHEN p.l10n_pt_independent_slip = 'true'
                     AND EXISTS (
                         SELECT 1
                         FROM hr_payslip_line l
                         WHERE l.slip_id = p.id
                           AND l.code = 'SUBS_NAT'
                     )
                    THEN 'christmas'
                WHEN p.l10n_pt_independent_slip = 'true'
                    THEN 'normal'
            END
        FROM hr_payroll_structure s
        JOIN res_country c ON c.id = s.country_id
        WHERE p.struct_id = s.id
          AND c.code = 'PT';
    """
    )
