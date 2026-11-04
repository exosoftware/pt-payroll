"""Absences now deduct the share of every rule that affects the hourly wage, so
the "Proportional Allowance" mechanism (a DES_* rule deducting each flagged
allowance in proportion to the absences) is gone.

Each rule that used it, and the shift regime allowances it was meant for, now
affect the hourly wage instead, which deducts the same share through the
absences. The DES_* rules are archived rather than deleted, since validated
payslips keep lines pointing at them; flagging their XML-IDs noupdate stops
the module update from trying to delete them once they leave the data file.
"""

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

_SHIFT_CODES = ("REG_2_TUR", "REG_3_TUR", "REG_4_TUR", "REG_5_TUR")
_DISCOUNT_RULES = (
    "rule_pt_discount_work_schedule_exemption",
    "rule_pt_discount_two_shift_regime",
    "rule_pt_discount_three_shift_regime",
    "rule_pt_discount_four_shift_regime",
    "rule_pt_discount_five_shift_regime",
)


@openupgrade.migrate()
def migrate(env, version):
    if openupgrade.column_exists(
        env.cr, "hr_salary_rule", "l10n_pt_proportional_allowance"
    ):
        env.cr.execute(
            """
            UPDATE hr_salary_rule SET l10n_pt_affects_hourly_wage = TRUE
            WHERE l10n_pt_proportional_allowance
            """
        )
        _logger.info(
            "%s proportional allowance rule(s) now affect the hourly wage.",
            env.cr.rowcount,
        )

    # The flags are set by the chart template only on companies created after
    # install; follow it only where it already ran (the base wage is flagged).
    env.cr.execute(
        """
        UPDATE hr_salary_rule SET l10n_pt_affects_hourly_wage = TRUE
        WHERE code IN %s
          AND EXISTS (
              SELECT 1 FROM hr_salary_rule
              WHERE code = 'BASIC' AND l10n_pt_affects_hourly_wage
          )
        """,
        (_SHIFT_CODES,),
    )
    _logger.info("%s shift regime rule(s) now affect the hourly wage.", env.cr.rowcount)

    env.cr.execute(
        """
        UPDATE ir_model_data SET noupdate = TRUE
        WHERE module = 'ptplus_payroll' AND name IN %s
        RETURNING res_id
        """,
        (_DISCOUNT_RULES,),
    )
    rule_ids = tuple(row[0] for row in env.cr.fetchall())
    if rule_ids:
        env.cr.execute(
            "UPDATE hr_salary_rule SET active = FALSE WHERE id IN %s", (rule_ids,)
        )
        _logger.info("%s proportional discount rule(s) archived.", env.cr.rowcount)

    # Copies of those rules made by hand have no XML-ID, but call the same
    # helper, which no longer exists: computing a payslip would fail.
    env.cr.execute(
        """
        UPDATE hr_salary_rule SET active = FALSE
        WHERE active
          AND (condition_python LIKE '%%pt_get_proportional_allowance%%'
               OR amount_python_compute LIKE '%%pt_get_proportional_allowance%%')
        """
    )
    _logger.info("%s custom proportional discount rule(s) archived.", env.cr.rowcount)
