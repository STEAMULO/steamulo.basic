![Build Status](https://github.com/STEAMULO/steamulo.basic/actions/workflows/test.yml/badge.svg?branch=master)

Steamulo Basic
=========

Development
------------

This role use the [molecule framework](https://molecule.readthedocs.io/en/stable/) in order to simplify the development process.

Requirements:
* [Python 3](https://www.python.org/download)
* [Docker](https://docs.docker.com/get-docker/)

Setup your local environnement with python virtualenv prior to using molecule : `. venv.sh`

This command will create a virtual env, activate it and download python dependencies.

Use ```molecule converge``` to create a local environnement and ```molecule login``` to log into the test machine.

Before any commit ensure that every test are passing with ```molecule test```

License
------------

BSD

Author Information
------------

Steamulo - www.steamulo.com
