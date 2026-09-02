
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

Changelog
=========

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
