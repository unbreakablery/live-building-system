Live Building Sysem
======

Goal: Spin up a basic Flask application, connect it to a local SQLite database, add fake meter
data to the db, then implement a RESTful application for displaying the fake meter data in .json
format.


Install
-------

    # clone the repository
    $ git clone https://github.com/***user***/lbs
    $ cd lbs
    
Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install Flask:
    $ pip install flask

Run
---

::

    $ export FLASK_APP=app
    $ export FLASK_DEBUG=1
    $ python3 project/init_db.py
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=app
    > set FLASK_DEBUG=1
    > py -3 project/init_db.py
    > flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    $ pip install pytest
    $ python3 -m pytest