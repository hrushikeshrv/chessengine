.. _usage:

Usage & Installation
====================

.. note::
    **chessengine** requires Python 3.7 or later.

To just use the chessengine, the recommended method of installation is using pip -

.. code-block:: console

    $ pip install chessengine

To start a game on the command line, call the play module using -

.. code-block:: console

    $ python -m chessengine.play

Also see :ref:`playing_a_game` for more.

.. _dev_installation:

Installing Locally For Development
----------------------------------

For contributing to chessengine, you should get the source code by cloning the repository instead of
installing using `pip`.

First, fork the repository on GitHub.

Navigate to the folder where you want to download the source code, and then clone the repository
by running the following command -

.. code-block:: console

    $ git clone https://github.com/<your-username>/chessengine.git

Replace ``<your-username>`` with your GitHub username.

This will download the latest copy of the source code. Now, you can install it like a package using
`pip`. But first, it is highly recommended to create a virtual environment so that this installation
of chessengine doesn't interfere with other installations of chessengine on your machine (if you
have any).

To create a virtual environment in the directory in which you have cloned the repo, run the
following command -

.. code-block:: console

    $ python -m venv venv

This will create a virtual environment in a sub-directory called `venv`. Note that everytime you
make some changes to the source code, you will only be able to notice them if the virtual
environment is active. Activate the virtual environment using -

.. _activating_virtual_env:

.. code-block:: console

    $ source venv/bin/activate

.. note::

    If you are on Windows, you can activate your virtual environment by running -

    .. code-block:: console

        $ venv\scripts\activate

Now that you have activated the virtual environment, you can install chessengine.

.. code-block:: console

    $ pip install -e path/to/chessengine

Now, inside this virtual environment, the installed version of chessengine will point towards the
repository you just cloned, so you will immediately see any changes you make to the source code.

To work on a patch and make a pull request, see :ref:`contributing`