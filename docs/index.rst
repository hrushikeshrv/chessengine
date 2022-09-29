.. chessengine documentation master file, created by
   sphinx-quickstart on Sat Sep 24 08:53:11 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to chessengine's documentation!
=======================================

A chess engine written in Python with no dependencies.

.. note::

   This project is under active development and you may run into bugs, especially in the game loop.

Features
========

* Internal bitboard representation
* Alpha-beta pruned search
* Move generation API
* Opening book
* PGN parsing

Usage
=====

Installation
------------
See :ref:`usage` for detailed installation instructions.

Install using pip:

.. code-block:: console

   $ pip install chessengine

Start a game -

.. code-block:: console

   $ python -m chessengine.play

Table Of Contents
=================

.. toctree::
   api
   chessboard
   usage
   playing
   contributing
   :maxdepth: 2




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
