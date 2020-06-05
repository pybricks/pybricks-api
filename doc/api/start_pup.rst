Powered Up Quick Start
########################

This page shows how you can install Pybricks on your hub and run your first
program. When you're ready, browse through the Pybricks Modules in the left
hand menu to modify the example program.

.. warning::

    - **This is still in beta! Not everything may work as expected yet.**

    - **As with any beta software, proceed with caution.**

    - At the moment, only the **Control+ Hub** is ready for beta use.

    - We welcome your questions, feedback and bug reports on our `support page`_.

Preparing your computer
--------------------------------

Make sure that Bluetooth is enabled on your device and go to
`code.pybricks.com`_.

Right now, we officially support only Google Chrome, *version 85 or newer*.
It is currently available as a beta/developer version. You can install
it on Windows, Mac, and Linux without affecting your existing browser or data.
Download it `from here`_.

.. toggle-header::
    :header: **Extra steps for Linux users**

    - In Google Chrome or Chromium, go to ``chrome://flags/``.
    - Search for *Experimental Web Platform features*.
    - Enable it.



Installing the Pybricks firmware
--------------------------------

Pybricks uses an improved firmware that can run autonomous programs.
Installing it is easy:

.. raw:: html

    <video controls src="http://pybricks.com/wp-content/uploads/2020/06/install.mp4" width="100%"></video>

If you can't want watch the video, just follow these steps:

- Make sure your batteries are fresh.
- Make sure the hub is off.
- Press and hold the green button.
- Wait for the light to blink, but keep holding the button.
- On the Pybricks Code page, click the firmware update button.
- Select the ``LEGO Bootloader`` and click *Pair*.
- The light should change to a red/green/blue sequence.
- You can now release the button.
- Wait for the update to finish, indicated by a steady blue light.
- If you use the recommended browser, this will take about 90 seconds.

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
.. _support page: https://github.com/pybricks/support/issues/
.. _code.pybricks.com: http://code.pybricks.com/
.. _from here: https://www.google.com/chrome/dev/
