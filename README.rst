github-setup-irc-notifications
==============================

Configure all repositories in an organization with irc notifications

Usage
-----

.. code:: bash

    $ github-setup-irc-notifications --username kragniz boatd '#abersailbot'

.. code::

    $ github-setup-irc-notifications -h
    usage: github-setup-irc-notifications [-h] [--username USERNAME]
                                          [--password PASSWORD]
                                          organization channel

    positional arguments:
      organization         organization containing the repositories to add
                           notifications to
      channel              irc channel to send notifications to

    optional arguments:
      -h, --help           show this help message and exit
      --username USERNAME  github username
      --password PASSWORD  password for github user


Installation
------------

Requirements
------------

github-setup-irc-notifications depends on the great github3.py library by
@sigmavirus24. You can install it and any other dependencies with ``pip install
-r requirements.txt``.

Licence
-------

MIT - see COPYING for full licence.

Authors
-------

`github-setup-irc-notifications` was written by `Louis Taylor <louis@kragniz.eu>`_.
