Secret Messages
===============

We want to store "secret" messages in an image file.  The usual way is to
store the text characters in the low-order bits of
the image pixel data in such a way that we can reconstruct the original text.
We will write two programs:

* The "encoder" program will take an image file and a text message and produce
  a new image file containing the text.
* The "decoder" program will take the original image file and the encoded image
  file and produce the original text.

Warning: This method of storing text messages in an image file is not all that
secret.  Programs exist that look for non-random changes in the low-order bits
of image pixel data.

Along the way we will touch on various points:

* converting text messages to/from N bit value streams
* processing pixel data from image files
* handling Unicode messages

The etude starts
`here <https://github.com/rzzzwilson/PythonEtudes/wiki/Secret_Messages.00>`_,
and the code is
`here <https://github.com/rzzzwilson/PythonEtudes/tree/master/Secret_Messages>`_.
