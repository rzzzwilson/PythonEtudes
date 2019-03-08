+------------------------------------------------------------------------------+
| Table of Contents                                                            |
+==============================+===============================================+
| `Overview`_                  | What is this all about?                       |
+------------------------------+-----------------------------------------------+
| `From CLI to GUI`_           | Adding two numbers together                   |
+------------------------------+-----------------------------------------------+
| `Expression Recognizer`_     | Recognize simple expressions                  |
+------------------------------+-----------------------------------------------+
| `Hangman`_                   | Play the game of Hangman                      |
+------------------------------+-----------------------------------------------+
| `Two jugs problem`_          | Solve the "two jugs" problem                  |
+------------------------------+-----------------------------------------------+
| `Command line menus`_        | Menus for the command line                    |
+------------------------------+-----------------------------------------------+
| `Text Adventure`_            | Write a simple text adventure                 |
+------------------------------+-----------------------------------------------+
| `Secret Messages`_           | Encode a message in an image                  |
+------------------------------+-----------------------------------------------+

Welcome to the Python Etudes wiki!

Overview
========

This is a collection of short essays (etudes) on various subjects showing how
some problem could be solved in python.  The approach is to start very simply
and progress through various versions of a program, adding things like error
checking, better code structure, etc, as we go.  Along the way we will
demonstrate common errors often tripped over by beginners.

The code for the etudes is stored
`here <https://github.com/rzzzwilson/PythonEtudes/>`_ and the explanatory notes
for each etude are in this wiki.

All code is written for python 3.6 or later.

If you follow one of these etudes and you find a part not easy to understand or,
worse, wrong, please send me an email: rzzzwilson@gmail.com .

From CLI to GUI
===============

This etude is concerned with adding two numbers together, starting with a CLI
implementation, progressing through various levels of sophistication and then
moving into a GUI solution, using tkinter.  The notes start
`here <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.0>`_.
The code for this etude is
`here <https://github.com/rzzzwilson/PythonEtudes/tree/master/From_CLI_to_GUI>`_.

Expression Recognizer
=====================

Write a console program that:

1. accepts "int op int", print result, op = +-/* (require spaces)
2. allow "float op float", same ops
3. allow "name = exp", "name", same ops, single char names
4. allow power op "**", mod op "%"
5. allow multi-char names  <-- general parser introduced here
6. allow pseudo-ops, like "@vars", "@del name", etc
7. introduce bit ops, "<<", ">>", "&", "|", "~" and "^
8. introduce logical operators "&&", "||"
9. allow general expression, same ops plus parentheses
10. allow builtin functions like "pow(a, 2)", "ln(a)", etc
11. allow user-defined functions

At some point relax "require spaces" rule.

Also write a GUI version.

The etude starts 
`here <https://github.com/rzzzwilson/PythonEtudes/wiki/Expression_Recognizer.00>`_,
and the code is 
`here <https://github.com/rzzzwilson/PythonEtudes/tree/master/Expression_Recognizer>`_.

Hangman
=======

Not yet written.

Starting with the question on /r/learnpython:

https://www.reddit.com/r/learnpython/comments/9t6h2t/how_can_i_improve_on_my_code_for_hang_man_game/

write a command line solution and then, as before, progress to a GUI solution
using tkinter.

Two jugs problem
================

Not yet written.

Starting with a question on /r/learnpython:

https://ps.reddit.com/r/learnpython/comments/9y54oz/trying_to_create_create_code_you_have_2_jugs_of/

write a command line solution.

Command line menus
==================

Not yet written.

Taking the idea from `cli_input <https://github.com/rzzzwilson/cli_input>`_,
develop CLI menus.

Text Adventure
==============

Not yet written.

Inspired by the myriad cries for help on /r/learnpython (after getting shooed
of at /r/python!) to fix bugs in a simple text adventure.  Must be an assignment
somewhere.

Various stages:

* simple "walk around" adventure, discuss methods of storing data, discuss "forward reference" problem
* add features like short descriptions if recently at a place
* add objects that the player can pick up
* add monsters that can't move
* allow monsters to move
* discuss creating data and "data editors", "sanity" checker, etc

Secret Messages
===============

Write a suite of programs to hide text messages in image files.  One program
will take an image file and a text message and "hide" the message in the pixel
data.  Another program will take two images (original and encoded) and reproduce
the text message.

There are lots of lovely details here:

* get N bit values one at a time from a text message
* convert a stream of N bit values back to a text message
* get and modify pixel data from an image file

Inspired by
`this /r/learnpython thread <https://www.reddit.com/r/learnpython/comments/ag31z6/list_and_int_error_not_sure_what_to_do_lsb_steg/>`_.

The etude starts
`here <https://github.com/rzzzwilson/PythonEtudes/wiki/Secret_Messages.00>`_.
The code is
`here <https://github.com/rzzzwilson/PythonEtudes/tree/master/Secret_Messages>`_.

