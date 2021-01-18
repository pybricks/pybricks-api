Accessing advanced EV3 features
===============================

MicroPython runs on top of `ev3dev`_, which is a specific version of Linux.
Linux is an *operating system*. (Other popular operating
systems are Microsoft Windows and Apple macOS.) This means that your EV3 is
almost like a real computer, just much smaller.

The Linux command line
-----------------------------------------

Although your EV3 Brick is quite like a real computer, you do not interact with
it using a big screen and a mouse. Instead, you can access files and programs
on it using the *command line*. It is also called the *terminal*.

Follow the steps in :numref:`fig_terminal` to access the command line. Now
you can enter commands by typing them in and pressing enter.

.. _fig_terminal:

.. figure:: ../../api/images/terminal_label.png
   :width: 100 %
   :alt: files
   :align: center

   Opening the Linux command line and running the ``ls`` command.

**Running basic commands**

For example, if you type the following command and press enter::

   ls

then you will see the contents of the current folder. :numref:`fig_terminal`
shows the result: it listed the project folder of the ``getting_started``
project that we just ran.

If you type the following command and press enter::

   exit

then the command line will be closed. Alternatively, click the garbage icon
shown in :numref:`fig_terminal`.

You can copy text from the command line by selecting it and
then pressing ``ctrl`` ``shift`` ``c``.
You can paste text into the command line
using ``ctrl`` ``shift`` ``v``.

**Running commands as an administrator**

Some commands require a password to run. This is similar to administrative
tasks on your computer or tablet, such as installing a new app. These commands
work like any other command, but you add ``sudo`` in front of
them.

As an exercise, you can run the following command to turn the EV3 Brick off::

   sudo poweroff

You will be prompted for a password. Type ``maker`` and then press ``Enter``.

.. warning::

   Only run commands with ``sudo`` if you know what you are doing.

**Learning more about the command line**

To learn more about the command line and many of the available commands, we
recommend reading the beginner-friendly free ebook
called `The Linux Command Line`_.

To learn more about ev3dev-specific tips and tricks, visit the `ev3dev`_
website.

.. _hostname:

Changing the EV3 Brick name
-----------------------------------------------------------

When you search for your EV3 using Visual Studio Code, you see all EV3 Bricks
listed by their name. By default, all EV3 Bricks are named *ev3dev*. Follow
these steps to change that name:

   1. Open Visual Studio Code and connect to your EV3 as usual.
   2. Read the steps above about running commands as an administrator.
   3. Think of a good name. In this example, we'll
      call it ``autonomous-vehicle2``
   4. Enter the following command and press enter::

         sudo hostnamectl set-hostname autonomous-vehicle2

   5. Reboot the EV3 Brick for the change to take effect.
   6. You may need to reboot your computer as well.

EV3 Brick names should only contain lowercase letters ``a`` through ``z``,
the digits ``0`` through ``9``, and the hyphen ``-``. It must start with a
letter or digit. It cannot include spaces or other symbols.

.. _ev3dev: https://www.ev3dev.org/
.. _The Linux Command Line: http://linuxcommand.org/tlcl.php
