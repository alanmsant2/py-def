py-def
========

An alternative to python -c with much less typing, at the price of being dirtier.

**Installation**::

    $ pip install py-def

Usage
=====

If you have a file named foo.py with::

    def quite():
       return 5
    def loud():
        print 'hello'
    def double(arg):
       return arg*2

Instead of::

  $ python -c "import foo; foo.loud();"
  hello

You can now write::

    $ py-def foo 'loud()'
    hello

You can load multiple files::

  $ py-def foo,foo2 'loud()'
  hello

or directories::

  $ py-def ./,./dir1,./dir2/test.py 'loud()'
  hello

In cases where it works (e.g clashes between files are benign), you can **minimize your typing** and omit the first argument, the current directory is then loaded by default::

    $ py-def 'loud()'
    hello

Printing
========

Printing is handled for you::

    $ py-def foo 'quite()'
    5

The result of the call (if any) is printed, even though the function does not call 'print'.

More examples
=============

You can pass arguments to your functions::

    $ py-def foo 'double(2)'
    4

You can execute arbitrary code in your single line::

    $ py-def foo '"hot" if double(2) == 4 else "cold"'
    hot

This includes printing::

    $ py-def foo.py 'print "double {} is {}".format(2, double(2))'
    double 2 is 4

Rationale
=========
**Time** is our most valuable non-possesion. The python interpreter must be clean and unambiguous, including the way it handls it's option '-c'. However, more often than not, I will accept being dirty (e.g live with benign clashes between files) and simply type **py-def 'test23()'** as opposed to the double as long **python -c 'import foo.py; foo.test23()'**. Such dirty functionality should not be built into the interpreter, hence *py-def*: the tool playfully indicates its motivation by saving you from typing a space between 'python' and '-c'.
