Expression Recognizer
=====================

Write a console program that:

1. accepts "int op int", print result, op = +-/* (require spaces)
2. allow "float op float", same ops
3. allow power op "**", mod op "%"
4. allow "name = exp", "name", same ops, single char names
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
