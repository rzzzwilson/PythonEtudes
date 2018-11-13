+------------------------------------------------------------------------------+
| Table of Contents                                                            |
+==============================+===============================================+
| `Overview`_                  | what is this all about?                       |
+------------------------------+-----------------------------------------------+
| `From CLI to GUI`_           | adding two numbers together                   |
+------------------------------+-----------------------------------------------+
| `Expression Recognizer`_     | Recognize simple expressions                  |
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
