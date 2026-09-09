
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
-------------------------------------------------

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

9.7.1 (2026-09-08)
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

9.7.0 (2026-09-04)
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

9.6.0 (2026-09-02)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fixed the accumulated IRS figure shown under the IRS line: it was adding
  the previous payslip's withheld amount a second time on top of a total
  that already included it, overstating the difference between the two
  receipts.
- On a payslip with no base wage (for example, one carrying only overtime),
  the IRS breakdown printed under the IRS line no longer opens with a blank
  line.

9.5.0 (2026-08-27)
~~~~~~~~~~~~~~~~~~
**Features**

- Payslip batches now have a "Regenerate Entry" button. If the accounting
  entry generated for a batch turns out wrong - for example, a contract's
  cost center was fixed after the batch was already confirmed - this
  rebuilds the entry from the batch's current payslips without needing to
  reopen or redo the payslips themselves. If the entry was already posted,
  it is reset to draft first, kept in draft for review, and can be posted
  again once checked.

9.4.0 (2026-08-13)
~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Submitting the DMR online no longer ends with a technical error when the
  submission is recorded in the Tax Authority exchange log.

9.3.0 (2026-08-06)
~~~~~~~~~~~~~~~~~~
**Features**

- The Monthly Remuneration Statement (DMR-AT) can now be validated and
  submitted directly to the Tax Authority online, from the same assistant used
  to prepare it: after computing the statement you can send it, check its
  status, download the Tax Authority receipt and review any errors, reusing the
  DMR-AT file that is already generated. Exporting the file by hand remains
  available.

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
