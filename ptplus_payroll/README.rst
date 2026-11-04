
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

9.13.2 (2026-11-04)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- A payslip with deductions but nothing paid by bank, such as an independent
  receipt that only deducts a health insurance, showed 0 to receive and the
  deductions were never recovered. It now shows the negative amount to
  receive, as a payslip whose deductions exceed the salary already did. Once
  the payslip is confirmed, that amount can be reported on the employee's
  next payslip.

9.13.1 (2026-11-03)
~~~~~~~~~~~~~~~~~~~
**Improvement**

- The "Contracts Registered at Social Security" table of the employee form
  now shows one line per contract, with the terms in force. Social Security
  answers one record for each change of a contract's terms (for instance each
  raise), so a contract with several changes used to show as several
  contracts. The number of changes is shown on each line, and the
  "Information Periods" button lists all of them, grouped by contract.

9.13.0 (2026-10-26)
~~~~~~~~~~~~~~~~~~~
**Features**

- Time off types have a new "Social Security Leave" option, for the absences
  paid by Social Security (sickness, parenthood, family assistance). A time off
  type with this option must also have "Ignore Public Holidays" enabled, so
  public holidays count in the leave duration.
- The payroll treats every time off type with this option as a Social Security
  leave, also the ones you create: public holidays inside the leave count as
  days of absence on the DRI, the work entries keep the leave on those days,
  and a batch that spans two months extends the payslip up to the end of the
  leave within the month.
- The localization's time off types for sickness, occupational illness, family
  assistance, maternity and paternity now have both options enabled, also on
  existing databases. Their "Social Security Leave" option cannot be disabled.

9.12.1 (2026-10-23)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- On the employee form, the Social Security SCC check that tells whether
  Social Security holds the contract as it is in Odoo is now named "Contract
  Up to Date at SS". It had the same name as the indicator of a contract
  already communicated, so the two could not be told apart.
- Installing the module on a new database no longer fails when the link
  between time off and work entries is not installed yet: it is now
  installed together with the module.

9.12.0 (2026-10-23)
~~~~~~~~~~~~~~~~~~~
**Features**

- New Social Security SCC integration (Plataforma de Serviços de
  Interoperabilidade): companies that joined the new contributory cycle can
  now send the monthly remuneration values online, follow their processing
  and alerts, compare the values assessed by the Segurança Social with the
  payroll figures, worker by worker, and confirm the
  monthly contributory obligation - all from Payroll > Reporting > Portugal >
  Social Security SCC. A daily synchronization keeps the statements up to
  date and reminds the payroll managers before the confirmation deadline
  (the 20th of the following month); "Refresh Status" does the same for one
  statement on demand - the processing state of what was sent and, once the
  month is over, the values Social Security assessed. A month is only sent
  once Social Security holds the contracts of its payslips as they are in
  Odoo: otherwise the statement lists the employees whose contract has to be
  checked or communicated first. A new permanent remuneration still to
  communicate does not stop the month, but the statement names the employees
  concerned, since Social Security assesses the month from the remunerations
  it holds. The "Statement Lines" button opens the
  lines of a statement in a list of their own, to filter, group and export
  them. The expected obligation shown next to
  the assessed one is computed on the declared values, so each month carries
  the obligation of what it declares even when a payslip withholds
  contributions on values declared with the previous month. Once a month is
  confirmed, its values are locked and the confirmation receipt issued by
  Social Security can be downloaded from the statement; while Social Security
  still takes new communications, a payroll manager can reopen the month to
  correct and send it again. When Social Security refuses the
  confirmation - for instance because the deadline has passed - the month is
  marked as not confirmed and shows the answer it returned, so the month can
  be confirmed again once the situation is settled.
- Absences and overtime of the payslips are declared as Social Security
  expects them: absences reduce the days and the base remuneration of the
  month, and every value is declared with the month it belongs to - overtime
  worked in one month and paid in the next is declared with the month in which
  it was worked, and an absence of an earlier month corrected in this payslip
  is not declared here. Since Social Security replaces values instead of
  adding them up, both cases are handled by declaring the month they belong
  to: that month is flagged as to be sent again, and computing it again
  includes what the later payslips brought, ready to be sent to Social
  Security. Until a month is confirmed its values can be computed and sent
  again at any time - each communication replaces the previous one - so a
  disagreement with the values assessed by Social Security is settled by
  fixing the payslips and sending the month again. Every communication keeps
  its own history: opening a submission shows the exact values it sent and
  the state and alert Social Security reported for each of them, even after
  the month is recomputed and sent again. A month only moves to
  Assessed when Social Security makes its final assessment, after the month
  ends - until then the values it returns are provisional. Each statement
  has a responsible user (by default whoever created it): the reminders and
  warnings the statement raises - month to send again, confirmation
  deadline approaching, payment document expired - are addressed to that
  user.
- New Payroll settings: SCC membership and the credentials of the Social
  Security interoperability platform (PSI) - the Segurança Social Direta
  NISS and password - with the password stored encrypted and a connection
  test button.
- After joining the SCC, exporting the classic DRI file is blocked, since
  Social Security rejects it for member companies.
- New worker communications to Social Security, sent on demand from the
  employee's contract: "Communicate Employment Relationship" sends each new
  contract of the worker - the first one and any later contract, such as the
  one following a fixed term - due before the contract starts; "Communicate
  Contract Change" updates instead the contract Social Security already
  holds - the renewal of a fixed term, a new modality or remuneration - from
  the date the contract version takes effect, which is what Social Security
  expects while the worker's employment relationship is still open there
  (it refuses a new one for the same period); "Communicate Cessation" ends
  the worker's employment relationship at Social Security at the contract's
  end date - legally due by the 10th of the following month - with the
  Social Security reason derived from the reason for the end of contract
  when it maps to a single one, whether it is communicated for unemployment
  purposes, and the justification Social Security requires for some
  termination agreements; "Communicate Workplace Transfer" moves the worker
  at Social Security to another of the employer's workplaces, from the date
  of the contract version that changes it; "Communicate
  Permanent Remuneration" sends the
  remunerations the contract updates - base wage, cash allowance, seniority
  payments, working schedule exemption and the holiday and Christmas
  allowance twelfths - legally due by the 10th of the month following the
  change. Whenever a contract changes one of those and it was not
  communicated yet, the employee form warns about it. Each contract is
  communicated once: further changes require a new contract. Since Social
  Security issues no receipt for these, every accepted communication is kept
  with what was sent, who sent it and when, listed in the employee's
  communication history. "Check at SS" - on the employee form, or for many
  employees at once from the employees list - keeps on the employee form, in
  two tables, the contracts Social Security has registered for the worker
  (dates, modality, base remuneration, reason) and the permanent
  remunerations it has on record over all of them (type, dates, value). The
  contract is marked as communicated when Social Security holds it as it is
  in Odoo, and the remunerations when it holds exactly the ones the contract
  defines - for instance communicated directly at Segurança Social Direta;
  when it holds other values, they are offered to communicate. The check
  also reads back the state of
  the employment relationships communicated: Social Security accepts them
  at entry and processes them later, so each one shows as being processed,
  integrated or refused with the reason - a refusal, also checked daily, is
  raised to whoever sent it and lets the contract be communicated again.
  The communications offered follow that query: until the worker is checked
  only the two queries are available; afterwards the employment relationship
  is offered when Social Security has none open, a contract change when it
  holds an open relationship from another contract or this contract with
  another end, and the cessation once the contract it holds ends (not when
  another contract follows right away). A contract change is offered on the
  contract's latest version only, and in the order Social Security takes
  them: a contract it does not know yet goes from its start date with that
  version's terms, one it holds with another end changes from the date the
  version takes effect.
  Every communication checks the worker at Social Security again right
  before sending, and when Social Security is no longer in the expected
  state nothing is sent and the user is told what to communicate instead.
  Once Social Security accepts a contract change or a cessation, the
  contracts are read back on their own, so the form shows them up to date.
- Paying the contributions: once Social Security has assessed a month, the
  new Payment tab of the SCC statement requests the payment document from
  Social Security and shows what it issued - document number, amount,
  validity, Multibanco entity and reference, IBAN. Social Security issues the
  document for the employer contributions currently owed, so a request may
  bring more than one document, each followed on its own. A document is
  marked as paid when Social Security reports the payment in its receipts
  (checked daily), or by hand when it was paid before that; a document that
  expires unpaid is flagged on the statement and whoever confirmed the month
  is asked to request a new one. The statements list shows the payment
  situation of each month. Nothing is posted in accounting: the bank
  statement reconciliation stays as it is today.

9.11.0 (2026-10-19)
~~~~~~~~~~~~~~~~~~~
**Improvement**

- In November 2026 the IRS withheld on salaries and pensions is half the value
  of the withholding tables, for employees of the Mainland and the Azores
  (Despacho n.º 12523-A/2026 and Despacho n.º 12610-A/2026). The reduction also
  applies to the holiday and Christmas allowances paid in that month, including
  independent receipts. Employees whose monthly pay falls in the last bracket
  of the tables, employees of Madeira, non-residents and employees with a fixed
  withholding rate keep the full withholding. From December 2026 the tables
  apply in full again.

9.10.0 (2026-10-19)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Absences, including the days before an admission or after a termination in
  the middle of the month, were deducted at the hourly wage of the base wage
  alone, while the hourly wage shown on the payslip also counts the other
  rules marked "Affects Hourly Wage" (diuturnities, work schedule exemption).
  Absences are now deducted at that same hourly wage.

**Improvement**

- The shift regime allowances now affect the hourly wage, so their share is
  deducted with the absence itself. The "Proportional Allowance" option on
  salary rules and the "Desconto Isenção Horário de Trabalho" / "Desconto
  Regime de N Turnos" lines are no longer needed and have been removed; rules
  that had the option checked now affect the hourly wage instead. Past
  payslips keep their discount lines.

9.9.16 (2026-10-13)
~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- The DMR and the DRI now include the payslips of the company's branches,
  since both are filed once per employer. Until now the DMR only reported the
  payslips of the main company, and the DRI those of the companies enabled in
  the company selector.

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
