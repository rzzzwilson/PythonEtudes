Expression Recognizer
=====================

Write a console program that:

1. accepts "int op int", print result, op = +-/* (require spaces)
2. allow "float op float", same ops
3. allow power op "**", mod op "%"  <-- general parser introduced here
4. extend parser to allow parentheses
5. allow "name = exp", "name", same ops, multi char names
7. allow pseudo-ops, like "@vars", etc
8. allow builtin functions like "pow(a, 2)", "ln(a)", etc

At some point relax "require spaces" rule.

Also write a GUI version.

The etude starts
`here <https://github.com/rzzzwilson/PythonEtudes/wiki/Expression_Recognizer.00>`_,

and the code is
`here <https://github.com/rzzzwilson/PythonEtudes/tree/master/Expression_Recognizer>`_.
