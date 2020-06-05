Powered Up Quick Start
########################

Coming soon!


Installing the Pybricks firmware
--------------------------------

.. raw:: html

    <video controls src="http://pybricks.com/wp-content/uploads/2020/06/install.mp4" width="100%"></video>


Running programs
--------------------------------



Saving a program permanently
--------------------------------------

When you run a program as shown above, it is deleted as soon as it's done.
That's because Powered Up hubs don't have a file system to store
programs. Fortunately, you can still save a script on the hub by including it
in the firmware.

Of course, this is a bit slow to do every time. We recommend the
using the standard procedure most of the time.
When you're happy with your final program, you can save it permanently as
described below. To change the program, just repeat these steps.

*Once installed, you can start that program with the green button.
No connection required!*

.. todo::

    **Coming soon! This will be made easy with the click of a button.**

    .. toggle-header::
        :header: **But I want it now! Show me the hard way!**

        **Installing a permanent program manually**

        The firmware is a ZIP archive containing the basic firmware and one
        ``main.py`` script:

        1. Go to the `latest builds`_.
        2. Click a build with a green checkmark.
        3. Download ZIP archive for your hub.
        4. Modify the ``main.py`` file as you like.
        5. Drag your modified ZIP file *onto* the firmware update button.
        6. The update now proceeds as usual.
        7. When it's done, start your program with the green button!

Note: all LEGO motors and sensors need a few seconds to boot. You don't
normally notice because you spend that time connecting. But with the
program already installed, you're way faster. So if you experience
problems, give your hub a few seconds before you start your program.

Restoring the LEGO Firmware
---------------------------

Pybricks uses the same update method as the LEGO apps; just with a different
firmware file. This means you can go back to the original firmware any time.
As shown in the video below, just put the hub in update mode and
connect using a LEGO app.

This video shows the Powered Up app in *create* mode. It has firmware for all
hubs. As usual, you may need to restart the app to detect the hub. If it fails,
try again with fresh batteries.

.. raw:: html

    <video controls src="http://pybricks.com/wp-content/uploads/2020/06/restore.mp4" width="100%"></video>


.. _latest builds: https://github.com/pybricks/pybricks-micropython/actions?query=workflow%3ABuild+
