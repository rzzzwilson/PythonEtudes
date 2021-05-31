The code here is for the "From CLI to GUI" etude. The
`explanatory text is in the wiki <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.0>`_.

The basic idea is:

* Make it print 1 + 2 = 3 (ie, use f-strings and variables a and b).
* Get the two numbers from the user using input().
* Add exception handling to tell the user the input was bad, ie, don't crash if the user types "abc" for a number.
* Allow the user to reenter a number if they get it wrong.
* If you haven't already, refactor the code for getting an integer into a function which you call twice.
* Add unit tests to make sure each step above is working.
* Change the code to get the numbers from the command line, ie test.py 1 2.
* Add all the steps above into the command line code (exception handling, function).
* Add help that is printed when the user types test.py -h on the command line.
* Now make a tkinter GUI version of the project.
* Design the gui so the user **can't** enter a bad number.
* Most designs will have a button meaning "add the two numbers". Make it impossible to press the button until you have two valid numbers.
* Remove the button, typing in two numbers automatically updates the result.
