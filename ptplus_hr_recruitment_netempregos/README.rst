
Portugal - Net-Empregos Job Board
=================================

Publishes your Odoo job offers on `Net-Empregos <https://www.net-empregos.com>`_,
one of the largest job boards in Portugal.


Installation
============

Just do it

Configuration
=============

#. In Odoo, go to *Recruitment > Configuration > Settings*, section
   *Net-Empregos*, and paste the API key you generated in the company area of
   net-empregos.com under "Chave API". The key belongs to the company it is
   entered in, so put it in the company whose job positions are to be
   advertised.
#. To save typing, set the job type once on each employee type
   (*Employees > Configuration > Employee Types*): the first advert of a
   position then arrives already proposing it. Internships come set to
   "Estágio"; Odoo no longer has full-time or part-time employee types, so
   those job types are picked on the advert.
#. Publish a job offer. Choose Net-Empregos as the job board and fill in the
   *Net-Empregos* tab that appears: the zone, the professional category and the
   job type are required by the platform.

Changelog
=========

1.0.0 (2026-08-28)
~~~~~~~~~~~~~~~~~~
**Features**

- New job board: publish, change and remove job offers on Net-Empregos.
- The zone, professional category and job type Net-Empregos advertises an offer
  under are asked for when publishing, on a *Net-Empregos* tab that only
  appears once that job board is chosen. So the job position stays free of a
  block of fields per job board, and two adverts for the same position can
  differ.
- Publishing the same position again starts from the last advert published for
  it on Net-Empregos, so only the very first advert is any typing. The job type
  is proposed from the employment type -- full-time, part-time and internship
  offers arrive already filled in -- when there is no earlier advert to go by.
- What an advert was published under is kept on the job board post and shown
  there, so it stays visible and can be changed with Update.
- The advert is published on the Net-Empregos account of the company the job
  position belongs to, and taken down from that same account. A position shared
  across companies uses the account of the company being worked in.

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
