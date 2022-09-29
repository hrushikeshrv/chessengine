.. _contributing:

Contributing A Patch
====================

Before contributing, make sure you have followed the steps given under :ref:`dev_installation`
and installed the development version of chessengine in a virtual environment. Before starting work
on your patch, make sure you have raised an issue about it on the project repository, or an issue
about the patch exists.

Once you have installed chessengine correctly, you should activate your virtual environment before
starting to work on a patch - see :ref:`activating virtual environment <activating_virtual_env>`.

Next, create a branch for your patch by running -

.. code-block:: console

    $ git checkout -b <branch-name>

You can name your branch anything you want. Then, write the code for your patch and modify the required files. If required, update the
documentation as well.

Commit your changes and add a commit message of the format - ``Fixed #<issue-number> -- <description>``,
where ``<issue-number>`` is the id of the issue you are trying to fix. As a last step, make sure
you have formatted your code using ``black``. Black is a PEP8 compliant opinionated formatter. If you
haven't already installed black, install it using -

.. code-block:: console

    $ pip install black

Then run it on the files you have changed by -

.. code-block:: console

    $ black path/to/changed/files

Finally, you can push your changes using -

.. code-block:: console

    $ git push origin <branch-name>

Now you can start a pull request!