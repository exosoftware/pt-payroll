Portugal - Payroll Salary Configurator
======================================

Makes Odoo's salary configurator work for Portuguese contracts:

- The offer preview computes the Portuguese payslip (IRS, Segurança Social,
  net salary). A candidate has no Portuguese tax data yet, so the preview
  assumes the income tax region and the Segurança Social regime set on the
  contract template.
- The employer cost of a contract counts the 14 yearly payments, the employer
  Segurança Social, the work accident insurance, the work schedule exemption
  (isenção de horário) and the meal allowance. The meal allowance carries no
  charges.
- The candidate fills in, on the offer, the information the payslip needs:
  marital status, number of holders, dependent children, NISS, NIF, income tax
  region, disability (and its degree, as a percentage) and pensioner status.

Installation
============

Installs automatically together with ``ptplus_payroll`` and the salary
configurator (``hr_contract_salary``).

Configuration
=============

- On a contract template, in **Salary Information**, set the work schedule
  exemption, the meal allowance, the meal allowance days per year and the work
  accident insurance rate. They feed the employer cost.
- In **Salary Simulation (PT)**, set the income tax region and the Segurança
  Social regime the offer preview assumes for a candidate. A hired employee
  keeps their own values: these are never written on them.
