Python 3 version of `Luke's Seating Planner <https://bitbucket.org/spookylukey/seating-planner/src/default/>`_
==================================================================================================================

|Python Version Support|

.. |Python Version Support| image:: https://img.shields.io/badge/python-3.7%7C3.8-green.svg
    :target: https://python.org/


Seating planner
===============

This app attempts to solve the problem of seating a group of guests at a wedding
(or other occasion) so that everyone knows people on their table.

The approach taken involves:

* Using a connection matrix that defines the strength of connections between all
  the guests, and using that to score a given arrangement. Credit for this goes to
  Meghan L. Bellows and J. D. Luc Peterson2

  http://www.improbable.com/news/2012/Optimal-seating-chart.pdf

* Using simulated annealing to attempt to find a good solution.

  The code for this comes from https://github.com/perrygeo/python-simulated-annealing


seating_planner/solver.py contains the main entry point for the algorithm

seating_planner/web_app.py contains a Flask web app as a UI, including a
relatively nice interface for entering the connection matrix.

Install
-----------------------
Python 3.7

Create a virtual environment and activate it

.. code-block::

    $ python -m pip install virtualenv
    $ python -m virtualenv venv
    $ /venv/scripts/activate

install the dep

.. code-block::

    $ (venv) python -m pip install -r requirements.txt


QuickStart
------------------------

Run the flask app:

.. code-block::

    $ python run.py

Go to http://localhost:5000

Add names in the "Names to Add:" block.

Work the Matrix by entering people based on their connection strength 50= together -50= apart 0= indifferent.

Can also include a connection matrix as a csv saved as a `.txt` file using the Upload connection data file upload button.

Run with PyPy for significant speedups (about 5-10x)

Deploying
--------------------------
It can de deployed using any WSGI container e.g. gunicorn:

.. code-block::

    $ gunicorn  -b 127.0.0.1:12345 -D -w 4 seating_planner.web_app:app


License
-------

seating_planner/anneal.py has its own copyright licence.

Other code is put into the public domain.
