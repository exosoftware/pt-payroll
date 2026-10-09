
Portugal - Payroll
===================

The base module for handling Portuguese payroll in Odoo. Mods include:

- X
- Y
- Z

Installation
============

Just do it

Configuration
=============

Salary rules declared in the previous month (DRI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some amounts are paid on one month's payslip but belong to the previous
month's remuneration: overtime, remuneration arrears, or a benefit the
employee only used after the payslip of the month it relates to. In the DRI
these must be declared under the previous month.

To have a salary rule declared that way, **end its code in ``_MES_ANT``** (for
example ``COVERFLEX_MES_ANT``). The rule is then declared under the month
before the one being reported, with the same income code it would otherwise
have - being paid later does not change the nature of the remuneration, so
keep the "DRI Code Subject" of the original rule.

The usual way to set one up is to duplicate the rule that already pays the
amount, add "(mês anterior)" to its name so it can be told apart on the
payslip, and give the copy a code ending in ``_MES_ANT``.

Two things to keep in mind:

- Only the ending counts: ``COVERFLEX_MES_ANT`` works, ``COVERFLEX_MES_ANT_2``
  does not.
- Do not put ``SUBS_REF`` in the code of such a rule. Codes containing it are
  treated as a meal allowance and split between the exempt and the subject
  amount, which takes precedence over the previous month.

The overtime rules named "(Mês Anterior)" and "Acertos de Remunerações ou
Retroativos" are already declared under the previous month and need no
change.

Changelog
=========

9.9.15 (2026-10-07)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Proportional holiday and Christmas allowances (and holiday allowance from
  previous years) were added on top of a full month's allowance to pick the IRS
  rate, so an exit payslip paying only the proportionals withheld at a much
  higher rate than due. The rate now follows a full month's allowance, or what
  was actually paid in the period when that is higher.

9.9.14 (2026-10-06)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Holiday and Christmas allowance twelfths withheld no IRS for employees whose
  contract started in the current year, because the amount used to pick the
  rate was left at zero. This also hit renewed and amended contracts of
  employees admitted in earlier years. The rate now follows the whole
  allowance, and only the year in which the employee was admitted counts as
  the admission year.

9.9.13 (2026-10-06)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- When an employee had two payslips in the same month and both paid holiday or
  Christmas allowance twelfths, the second payslip gave back the IRS the first
  one had withheld on its twelfth, instead of withholding on its own. The
  payslips withheld less IRS than the DMR declared. Each payslip now withholds
  the IRS on the twelfth it pays.

9.9.12 (2026-10-06)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- The total of contributions in the Declaração de Remunerações (DRI) file is
  now the declared remunerations times the contribution rate, rounded once.
  It used to add up each payslip's contributions, each rounded to the cent on
  its own, so the total could be a few cents off and Segurança Social accepted
  the file with alert DS24 ("valor de contribuições diferente do total de
  remuneração * taxa"). The contributions deducted on each payslip do not
  change.

9.9.11 (2026-10-02)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- With the holiday and Christmas allowance provisions active, a payslip could
  not be computed for an employee whose first contract date was empty. The
  provisions now take the start date of the employee's first contract instead.
  The field and its label on the employee form are now called "Data do Primeiro
  Contrato" and "Primeiro Contrato", so they no longer show the same label as
  the contract dates right above them.

9.9.10 (2026-10-01)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- When the dates of a saved receipt were moved to another month, it stayed
  chained to the receipt of the month it left. The old receipt then took the
  new month as its reference period, so the new receipt added its taxable base
  to the IRS of the month and withheld IRS as if it were a second receipt of
  that month, crediting the IRS of the other month. Moving a receipt to another
  month now unchains it from the receipts it left behind, which are chained
  again among themselves.

9.9.9 (2026-09-29)
~~~~~~~~~~~~~~~~~~
**Features**

- Temporary partial incapacity after an accident at work can now be recorded
  as a salary complement of the type "Incapacidade Temporária Parcial [%]",
  with the incapacity degree and the period it applies to. The payslip shows a
  deduction line that takes that percentage off the base wage and the other
  earnings that make up the hourly wage, only for the working hours inside the
  period, so the employee is paid for the remaining capacity. Days already
  discounted as unpaid absences are not discounted twice. When the degree
  changes, close the current period and create a new one: several degrees in
  the same month add up, and overlapping periods for the same employee are
  refused.
- To set that deduction by hand, add an input of the type "Incapacidade
  Temporária Parcial [valor]" to the payslip with the amount to deduct. That
  amount replaces the calculated one.

9.9.8 (2026-09-29)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- An employee who worked part of a day and was away for the rest of the month
  was declared with 0 days of work next to the pay received for those hours,
  in the DRI and in the holiday sheets file. That month now declares half a
  day. A whole month away still declares 0 days.

9.9.7 (2026-09-25)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- The days of work declared to Segurança Social in the DRI, and in the
  holiday sheets file sent to the work-accident insurer, are corrected in
  months with 31 days and in February. A whole month away declares 0 days,
  where it used to declare 1. In February, absences above half a month declare
  the days actually worked: an employee who only worked two days declares 2
  days instead of 4. Half days coming from absences registered in hours are
  kept, including above one day.
- An employee with more absences than days in the month could get a negative
  number of days, which broke the line in the file and made the insurer reject
  it. The days now always stay between 0 and 30, and the file can no longer be
  generated with an invalid line.
- When a payslip covers days of the previous month, the correction of that
  month never removes more days than were declared for it, so the month cannot
  end up below 0 days.
- From January 2026, part-time and hourly work is declared as one day per
  five hours, and one more day for any remaining hours, as set by Decreto
  Regulamentar n.º 7/2025. Half days are no longer used for these contracts.

9.9.6 (2026-09-14)
~~~~~~~~~~~~~~~~~~
**Improvement**

- The "Overtime - Conversion to Banco de Horas" rates are gone from the
  Portugal Localization settings and from the contract. Banco de Horas is
  set up by the module that implements it, which has its own "Banco de
  Horas (PT)" section in the same settings page; the rates here were a
  second, unused copy that never affected any calculation, so whichever of
  the two was filled in was a coin toss. Nothing to re-enter: the rates
  actually in force are the ones already in that section.

9.9.5 (2026-09-11)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- In a month where the absences to be discounted exceed half of the working
  time, the receipt pays what was worked and discounts the rest. That
  calculation now measures the time worked on the employee's own work
  schedule, minus the absences being discounted, instead of adding up the
  hours registered on the receipt. Two situations were being paid wrongly. An
  absence paid in full that was created directly as a work entry type, without
  a corresponding time off type, was neither discounted nor paid: the employee
  lost that money. And hours registered above the schedule, such as overtime,
  reduced the discount of the absences, which paid them a second time on top
  of their own line.

9.9.4 (2026-09-11)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Absences that are paid in full - licença de casamento, falecimento de
  familiar, trabalhador-estudante, ausências aprovadas pelo empregador,
  férias gozadas, and any other absence listed as paid on the salary
  structure - now count as time worked when the remaining absences are
  valued. A month with many paid absences used to be read as a month mostly
  absent: the absences that really are discounted were then valued by the
  proportional calculation, which also took away the pay of the absences the
  employer pays. Now only the discounted absences weigh on that decision and
  on the calculation, so a paid absence no longer costs the employee money.
  The hourly value used by "Assiduidade (mês anterior)" follows the same
  rule.

9.9.3 (2026-09-09)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- A receipt with expenses attached no longer shows an error and can be
  confirmed. Odoo expected the expenses to be paid by a single "Expenses"
  salary rule, which the Portuguese receipt does not use: it pays them through
  its own rules (ajudas de custo, deslocações em viatura própria, ...), each
  with its own account.

9.9.2 (2026-09-08)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Receipts that deduct absences from the previous month no longer add the
  "Segurança Social (Acerto de Quotizações ao Funcionário)" amount. Deducting
  the absence already lowers the receipt's Social Security base, so the
  contribution withheld that month already falls by exactly what had been
  withheld in excess on those days - the separate line was returning the same
  contribution a second time and left the net higher than it should be. The
  line is no longer processed; receipts already issued keep it and their values
  do not change. In the rare receipt where the deductions exceed the month's
  pay and no contribution is withheld at all, the previous month's contribution
  now has to be returned by hand.

9.9.1 (2026-09-08)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- The DMR now declares the Social Security deducted over amounts that are
  subject to Social Security but are not income for the AT - a correction to
  the contribution base of an earlier month, for instance. That contribution
  was being left out of the declaration, so the DMR reported less than the
  receipt had deducted.
- The IRS withheld on the receipt and the IRS declared on the DMR no longer
  differ by one euro. When the withholding landed exactly on a whole euro the
  receipt deducted one euro less than the amount the DMR declared; both now
  show the same value. Withholdings are still declared in whole euros, cents
  dropped, as before.

9.9.0 (2026-09-04)
~~~~~~~~~~~~~~~~~~
**Features**

- Salary rules can now be declared in the DRI under the previous month by
  ending their code in ``_MES_ANT``. Until now only the overtime rules named
  "(Mês Anterior)" and "Acertos de Remunerações ou Retroativos" were declared
  that way, and adding another one meant asking for a change to the module.
  New ones can now be created directly on the database - by duplicating the
  rule that pays the amount and giving the copy a code ending in ``_MES_ANT``
  - which covers amounts an employee only receives after the month they relate
  to. See the Configuration section.

9.8.0 (2026-09-02)
~~~~~~~~~~~~~~~~~~
**Improvement**

- Salary complements can now be searched by description and company, and
  filtered and grouped by status, employee, input type and whether they
  are an attachment. The list opens on the running ones.

**Bugfixes**

- Absences are now recognised by being a Time Off type, instead of by
  having "FALTA" in their code. An absence type created directly on a
  database, without following that naming convention, used to be counted
  as a worked day - it now counts as an absence everywhere it should: in
  the meal allowance, in the proportional allowances and in the previous
  month's hourly wage.
- Choosing a meal allowance payment method on an employee of a non-PT
  company no longer overwrites the amount with a Portuguese default.

9.7.0 (2026-08-27)
~~~~~~~~~~~~~~~~~~
**Features**

- Payslip batches now have a "Regenerate Entry" button. If the accounting
  entry generated for a batch turns out wrong - for example, a contract's
  cost center was fixed after the batch was already confirmed - this
  rebuilds the entry from the batch's current payslips without needing to
  reopen or redo the payslips themselves. If the entry was already posted,
  it is reset to draft first, kept in draft for review, and can be posted
  again once checked.

9.6.0 (2026-08-21)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- The payslip PDF title no longer overlaps the report header.
- The Social Security rate no longer wraps onto a second line in the Rate
  column.
- The contract wage period next to "Salário do Contrato" now shows in
  Portuguese (e.g. "Mensal") instead of the raw English value ("monthly").
- Fixed the accumulated IRS figure shown under the IRS line: it was adding
  the previous payslip's withheld amount a second time on top of a total
  that already included it, overstating the difference between the two
  receipts.

9.5.0 (2026-08-13)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Submitting the DMR online no longer ends with a technical error when the
  submission is recorded in the Tax Authority exchange log.

9.4.0 (2026-08-06)
~~~~~~~~~~~~~~~~~~
**Features**

- The Monthly Remuneration Statement (DMR-AT) can now be validated and
  submitted directly to the Tax Authority online, from the same assistant used
  to prepare it: after computing the statement you can send it, check its
  status, download the Tax Authority receipt and review any errors, reusing the
  DMR-AT file that is already generated. Exporting the file by hand remains
  available.

9.3.0 (2026-08-05)
~~~~~~~~~~~~~~~~~~
**Improvement**

- The payslip PDF now uses Odoo's standard payslip layout, complemented with
  the Portuguese details (profession, professional category, beneficiary and
  taxpayer numbers, insurance, hourly wage, reference pay period, IRS
  withholding breakdown and a payment information table with the amounts paid
  by bank transfer, in kind or by meal ticket/card). The employee and other
  information sections show the Portuguese fields even when they are not
  filled in, and the styling options available on salary rules (bold, italic,
  color, title, description) are now reflected on the printed receipt.

9.2.0 (2026-08-05)
~~~~~~~~~~~~~~~~~~
**Improvement**

- Regular attendance now uses Odoo's native "Attendance" work entry type
  (displayed as "Assiduidade" in Portuguese) instead of a duplicate type
  specific to this module. Existing payslips, working schedules and work
  entries are converted automatically when the module is updated, and the
  duplicate type is removed.

8.2.2 (2026-01-22)
~~~~~~~~~~~~~~~~~~
**Features**

- Income Statement Report is now able to be sent directly to the employee.
- Allow Income Statement Report to be saved to Documents.

Credits
========

Contributors
~~~~~~~~~~~~

* `Exo Software <https://exosoftware.pt>`_:

  * Tiago Rangel <tiago.rangel@exo.pt>
  * Pedro Castro Silva <pedrocs@exo.pt>

* `Growfactor <https://www.growfactor.pt>`_:

  * Álvaro Ribeiro <alvaro.ribeiro@growfactor.pt>
  * Luís Homem <luis.homem@growfactor.pt>


Maintainer
~~~~~~~~~~

This module is maintained by Exo Software, Lda.

.. image:: https://exosoftware.pt/logo.png
   :alt: Exo Software
   :target: https://exosoftware.pt
   :width: 100px
