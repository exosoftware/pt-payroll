
Portugal - SAPO Emprego Job Board
=================================

Publishes your Odoo job offers on `SAPO Emprego <https://emprego.sapo.pt>`_,
one of the largest job boards in Portugal.


Installation
============

Just do it

Configuration
=============

SAPO Emprego gives access to its API in two steps, and the module follows
them.

#. In the company area of `the test platform
   <https://emprego-sandbox.sapo.pt>`_, under "API", ask for a test token.
#. In Odoo, go to *Recruitment > Configuration > Settings*, section
   *SAPO Emprego*, leave the environment on **Test** and paste the token. The
   token belongs to the company it is entered in, so put it in the company
   whose job positions are to be advertised.
#. Press **Refresh from SAPO Emprego**. This reads the districts, professional
   categories, work hours, contract types, qualifications, experience levels,
   salary ranges and available positions from the platform. Nothing can be
   published before this, and from then on the lists refresh themselves once a
   day.
#. To save typing, set the work hours and contract type once on each
   employment type (*Employees > Configuration > Employment Types*) and the
   qualification on each degree
   (*Recruitment > Configuration > Degrees*): the first advert of a position
   then arrives already proposing them.
#. Publish a job offer. Choose SAPO Emprego as the job board and fill in the
   *SAPO Emprego* tab that appears: the country, the districts, the
   professional categories, the work hours and the annual salary range are
   required by the platform. Then send SAPO the address of the advert, shown on
   the job board post. Once they approve it, ask for a production token in the
   company area of the live platform, and in Odoo switch the environment to
   **Production** and paste the new token.

Changelog
=========

1.0.0 (2026-09-07)
~~~~~~~~~~~~~~~~~~
**Features**

- New job board: publish and change job offers on SAPO Emprego, and take them
  off its listings.
- Everything SAPO Emprego needs to describe an offer -- the country,
  districts, municipality, professional categories, work hours, contract type,
  qualification, experience, salary range, available positions, work model and
  CV requirement -- is asked for when publishing, on a *SAPO Emprego* tab that
  only appears once that job board is chosen. So the job position stays free of
  a block of fields per job board, and two adverts for the same position can
  differ.
- Publishing the same position again starts from the last advert published for
  it on SAPO Emprego, so only the very first advert is any typing. The work
  hours and contract type are proposed from the employment type of the
  position, and the qualification from its expected degree, when there is no
  earlier advert to go by.
- The lists are read from SAPO Emprego and refreshed daily, so a change on
  their side arrives on its own.
- SAPO Emprego does not publish web or email addresses inside an advert, so
  any that the job description carries are left out of it and named on the job
  board post. Candidates apply through the advert itself.
- The requirements of the job position fill the *Perfil* section of the
  advert, one requirement per line, and its skills fill *Competências*.
- The job position itself is asked for nothing: it keeps only what Odoo already
  holds about it.
- The same tab carries the wording of the advert: the line under the title,
  what the company offers, the working hours and any observations. Clearing one
  takes its section off the advert.
- Everything written for an advert is kept on the job board post and shown
  there, so what was published stays visible and can be changed with Update.
- The advert is published on the SAPO Emprego account of the company the job
  position belongs to, and taken down from that same account. A position shared
  across companies uses the account of the company being worked in.
- Applications are mailed to the email alias of the job position, so an
  application on SAPO Emprego becomes an applicant in Odoo on its own. A
  position without an alias cannot be published, and says so.
- The account is read back from SAPO Emprego, so its level and premium
  services are shown under Recruitment > Configuration > Settings.
- Choosing to redirect candidates to your own website is only passed on when
  the account has the premium service SAPO Emprego requires for it. Without
  it, the job board post says so and names the address the applications really
  arrive at, instead of the platform quietly ignoring the redirect.
- The address of the published advert is shown on the job board post, which is
  what SAPO asks for to approve production access.
- Offers can be published on the test platform first, and switched to
  production once SAPO approves the advert.

Credits
========

Contributors
~~~~~~~~~~~~

* `Exo Software <https://exosoftware.pt>`_:

  * Pedro Pereira <pedro.pereira@exo.pt>

Maintainer
~~~~~~~~~~

This module is maintained by Exo Software, Lda.

.. image:: https://exosoftware.pt/logo.png
   :alt: Exo Software
   :target: https://exosoftware.pt
   :width: 100px
