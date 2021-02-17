# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 The Pybricks Authors

"""Generic cross-platform module for typical devices like lights, displays,
speakers, and batteries."""

from .parameters import Direction, Stop


class DCMotor:
    """Generic class to control simple motors without rotation sensors, such
    as train motors."""

    def __init__(self, port,
                 positive_direction=Direction.CLOCKWISE):
        """

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive duty cycle value.
        """
        pass

    def dc(self, duty):
        """Rotates the motor at a given duty cycle (also known as "power").

        Arguments:
            duty (:ref:`percentage`): The duty cycle (-100.0 to 100).
        """
        pass

    def stop(self):
        """Stops the motor and lets it spin freely.

        The motor gradually stops due to friction."""
        pass

    def brake(self):
        """Passively brakes the motor.

        The motor stops due to friction, plus the voltage that
        is generated while the motor is still moving."""
        pass


class Control:
    """Class to interact with PID controller and settings.

        .. data:: scale

            Scaling factor between the controlled integer variable
            and the physical output. For example, for a single
            motor this is the number of encoder pulses per degree of rotation.
    """

    def limits(self, speed, acceleration, duty, torque):
        """Configures the maximum speed, acceleration, duty, and torque.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (:ref:`speed` or :ref:`linspeed`):
                Maximum speed. All speed commands will be capped to this value.
            acceleration (:ref:`acceleration` or :ref:`linacceleration`):
                Maximum acceleration.
            duty (:ref:`percentage`):
                Maximum duty cycle during control.
            torque (:ref:`torque`):
                Maximum feedback torque during control.
        """
        pass

    def pid(self, kp, ki, kd, integral_range, integral_rate, feed_forward):
        """Gets or sets the PID values for position and speed control.

        If no arguments are given, this will return the current values.

        Arguments:
            kp (int): Proportional position control
                constant. It is the feedback torque per degree of
                error: µNm/deg.
            ki (int): Integral position control constant. It is the feedback
                torque per accumulated degree of error: µNm/(deg s).
            kd (int): Derivative position (or proportional speed) control
                constant. It is the feedback torque per
                unit of speed: µNm/(deg/s).
            integral_range (:ref:`angle` or :ref:`distance`): Region around
                the target angle or distance, in which integral control errors
                are accumulated.
            integral_rate (:ref:`speed` or :ref:`linspeed`): Maximum rate at
                which the error integral is allowed to grow.
            feed_forward (:ref:`percentage`):
                This adds a feed forward signal to the PID feedback signal, in
                the direction of the speed reference. This value is expressed
                as a percentage of the absolute maximum duty cycle.
        """
        pass

    def target_tolerances(self, speed, position):
        """Gets or sets the tolerances that say when a maneuver is done.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (:ref:`speed` or :ref:`linspeed`): Allowed deviation
                from zero speed before motion is considered complete.
            position (:ref:`angle` or :ref:`distance`): Allowed
                deviation from the target before motion is considered
                complete.
        """
        pass

    def stall_tolerances(self, speed, time):
        """Gets or sets stalling tolerances.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (:ref:`speed` or :ref:`linspeed`): If the controller
                cannot reach this speed for some ``time`` even with maximum
                actuation, it is stalled.
            time (:ref:`time`): How long the controller has to be below this
                minimum ``speed`` before we say it is stalled.
        """
        pass

    def stalled(self):
        """Checks if the controller is currently stalled.

        A controller is stalled when it cannot reach the target speed or
        position, even with the maximum actuation signal.

        Returns:
            bool: ``True`` if the controller is stalled, ``False`` if not.
        """
        pass

    def done(self):
        """Checks if an ongoing command or maneuver is done.

        Returns:
            bool: ``True`` if the command is done, ``False`` if not.
        """
        pass

    def load(self):
        """Gets the load acting on the ``Motor`` or ``DriveBase``.

        This value is determined from the feedback torque that is
        needed to track the speed or position command given by the user.

        When coasting, braking, or controlling the duty cycle manually, the
        load cannot be estimated in this way. Then this method returns zero.

        Returns:
            :ref:`torque`: The load torque. It returns 0 if control
            is not active.
        """
        pass


class Motor(DCMotor):
    """Generic class to control motors with built-in rotation sensors."""

    control = Control()
    """The motors use PID control to accurately track the speed and
    angle targets that you specify. You can change its behavior through the
    ``control`` attribute of the motor. See :ref:`control` for an overview
    of available methods."""

    def __init__(self, port,
                 positive_direction=Direction.CLOCKWISE,
                 gears=None):
        """

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive speed value or
                angle.
            gears (list):
                List of gears linked to the motor.

                For example: ``[12, 36]`` represents a gear train with a
                12-tooth and a 36-tooth gear. Use a list of lists for multiple
                gear trains, such as ``[[12, 36], [20, 16, 40]]``.

                When you specify a gear train, all motor commands and settings
                are automatically adjusted to account for the resulting gear
                ratio.  The motor direction remains unchanged by this.
        """
        pass

    def angle(self):
        """Gets the rotation angle of the motor.

        Returns:
            :ref:`angle`: Motor angle.

        """
        pass

    def speed(self):
        """Gets the speed of the motor.

        Returns:
            :ref:`speed`: Motor speed.

        """
        pass

    def reset_angle(self, angle):
        """Sets the accumulated rotation angle of the motor to a desired value.

        Arguments:
            angle (:ref:`angle`): Value to which the angle should be reset.
        """
        pass

    def hold(self):
        """Stops the motor and actively holds it at its current angle."""
        pass

    def run(self, speed):
        """Runs the motor at a constant speed.

        The motor accelerates to the given speed and keeps running at this
        speed until you give a new command.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
        """
        pass

    def run_time(self, speed, time, then=Stop.HOLD, wait=True):
        """Runs the motor at a constant speed for a given amount of time.

        The motor accelerates to the given speed, keeps running at this speed,
        and then decelerates. The total maneuver lasts for exactly the given
        amount of ``time``.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            time (:ref:`time`): Duration of the maneuver.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """
        pass

    def run_angle(self, speed, rotation_angle, then=Stop.HOLD, wait=True):
        """Runs the motor at a constant speed by a given angle.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            rotation_angle (:ref:`angle`): Angle by which the motor should
                                           rotate.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """
        pass

    def run_target(self, speed, target_angle, then=Stop.HOLD, wait=True):
        """Runs the motor at a constant speed towards a
        given target angle.

        The direction of rotation is automatically selected based on the target
        angle. It does not matter if ``speed`` is positive or negative.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            target_angle (:ref:`angle`): Angle that the motor should
                                         rotate to.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the motor to reach the target
                         before continuing with the rest of the
                         program.
        """
        pass

    def run_until_stalled(self, speed, then=Stop.COAST, duty_limit=None):
        """Runs the motor at a constant speed until it stalls.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            then (Stop): What to do after coming to a standstill.
            duty_limit (:ref:`percentage`): Duty cycle limit during this
                command. This is useful to avoid applying the full motor
                torque to a geared or lever mechanism.

        Returns:
            :ref:`angle`: Angle at which the motor becomes stalled.
        """
        pass

    def track_target(self, target_angle):
        """Tracks a target angle. This is similar to :meth:`.run_target`, but
        the usual smooth acceleration is skipped: it will move to the target
        angle as fast as possible. This method is useful if you want to
        continuously change the target angle.

        Arguments:
            target_angle (:ref:`angle`): Target angle that the motor should
                                         rotate to.

        """
        pass

    def dc(self, duty):
        """Rotates the motor at a given duty cycle (also known as "power").

        This method lets you use a motor just like a simple DC motor.

        Arguments:
            duty (:ref:`percentage`): The duty cycle (-100.0 to 100).
        """


class Speaker:
    """Plays beeps and sounds using a speaker."""

    def beep(self, frequency=500, duration=100):
        """Play a beep/tone.

        Arguments:
            frequency (:ref:`frequency`):
                Frequency of the beep. Frequencies below 100
                are treated as 100.
            duration (:ref:`time`):
                Duration of the beep. If the duration is less
                than 0, then the method returns immediately and the frequency
                play continues to play indefinitely.
        """
        pass

    def play_notes(self, notes, tempo=120):
        """Plays a sequence of musical notes. For example:
        ``['C4/4', 'C4/4', 'G4/4', 'G4/4']``.

        Each note is a string with the following format:

            - The first character is the name of the note, ``A`` to ``G``
              or ``R`` for a rest.
            - Note names can also include an accidental ``#`` (sharp) or
              ``b`` (flat). ``B#``/``Cb`` and ``E#``/``Fb`` are not
              allowed.
            - The note name is followed by the octave number ``2``
              to ``8``. For example ``C4`` is middle C. The octave changes
              to the next number at the note C, for example, ``B3`` is the
              note below middle C (``C4``).
            - The octave is followed by ``/`` and a number that indicates
              the size of the note. For example ``/4`` is a quarter note,
              ``/8`` is an eighth note and so on.
            - This can optionally followed by a ``.`` to make a dotted
              note. Dotted notes are 1-1/2 times as long as notes without a
              dot.
            - The note can optionally end with a ``_`` which is a tie or a
              slur. This causes there to be no pause between this note and
              the next note.

        Arguments:
            notes (iter):
                A sequence of notes to be played.
            tempo (int):
                Beats per minute. A quarter note is one beat.
        """
        pass

    def play_file(self, file):
        """Plays a sound file.

        Arguments:
            file (str):
                Path to the sound file, including the file extension.
        """

        pass

    def say(self, text):
        """Says a given text string.

        You can configure the language and voice of the text using
        :meth:`set_speech_options`.

        Arguments:
            text (str): What to say.
        """

        pass

    def set_speech_options(self, language=None, voice=None, speed=None, pitch=None):
        """Configures speech settings used by the :meth:`say` method.

        Any option that is set to ``None`` will not be changed. If an option
        is set to an invalid value :meth:`say` will use the default value
        instead.

        Arguments:
            language (str):
                Language of the text. For example, you can choose ``'en'``
                (English) or ``'de'`` (German). [#espeak_lang]_
            voice (str):
                The voice to use. For example, you can choose ``'f1'`` (female
                voice variant 1) or ``'m3'`` (male voice variant 3).
                [#espeak_lang]_
            speed (int):
                Number of words per minute.
            pitch (int):
                Pitch (0 to 99). Higher numbers make the voice higher pitched
                and lower numbers make the voice lower pitched.
        """
        pass

    def set_volume(self, volume, which='_all_'):
        """Sets the speaker volume.

        Arguments:
            volume (:ref:`percentage`):
                Volume of the speaker.
            which (str):
                Which volume to set. ``'Beep'`` sets the volume for
                :meth:`beep` and :meth:`play_notes`. ``'PCM'`` sets the volume
                for :meth:`play_file` and :meth:`say`. ``'_all_'`` sets both
                at the same time.
        """
        pass


class Light:
    """Control a single-color light."""

    def on(self, brightness=100):
        """Turns on the light at the specified brightness.

        Arguments:
            brightness (:ref:`brightness`):
                Brightness of the light.
        """

    def off(self):
        """Turns off the light."""
        pass

    def blink(self, durations):
        """Blinks the light by turning it on and off for given durations.

        The light keeps blinking indefinitely while the rest of your
        program keeps running.

        This method provides a simple way to make basic but useful patterns.
        For more generic and smooth patterns, use :meth:`.animate` instead.

        Arguments:
            (list): List of (:ref:`time`) values of the
                form ``[on_1, off_1, on_2, off_2, ...]``.
        """

    def animate(self, brightness_values, interval):
        """Animates the light with a list of brightness values. The next
        brightness value in the list is shown after the given interval.

        The animation runs in the background while the rest of your program
        keeps running. When the animation completes, it repeats.

        Arguments:
            brightness_values (list): List of :ref:`brightness` values.
            interval (:ref:`time`): Time between brightness updates.
        """

    def reset(self):
        """Resets the light to the default system behavior or animation."""
        pass


class ColorLight:
    """Control a multi-color light."""

    def on(self, color):
        """Turns on the light at the specified color.

        Arguments:
            color (Color): Color of the light.
        """
        pass

    def off(self):
        """Turns off the light."""
        pass

    def blink(self, color, durations):
        """Blinks the light at a given color by turning it on and off for given
        durations.

        The light keeps blinking indefinitely while the rest of your
        program keeps running.

        This method provides a simple way to make basic but useful patterns.
        For more generic and multi-color patterns, use ``animate()``
        instead.

        Arguments:
            color (Color): Color of the light.
            durations (list): List of (:ref:`time`) values of the
                form ``[on_1, off_1, on_2, off_2, ...]``.
        """

    def animate(self, colors, interval):
        """Animates the light with a list of colors. The next
        color in the list is shown after the given interval.

        The animation runs in the background while the rest of your program
        keeps running. When the animation completes, it repeats.

        Arguments:
            colors (list): List of :class:`Color <.parameters.Color>` values.
            interval (:ref:`time`): Time between color updates.
        """

    def reset(self):
        """Resets the light to the default system behavior or animation."""
        pass


class LightArray:
    """Control an array of single-color lights."""

    def __init__(self, n):
        """Initializes the light array.

        Arguments:
            n (int): Number of lights
        """
        pass

    def on(self, brightness):
        """Turns on the lights at the specified brightness.

        Arguments:
            brightness (tuple of :ref:`brightness`):
                Brightness of each light, in the order shown above. If you give
                one brightness value instead of a tuple, all lights get the
                same brightness.
        """
        pass

    def off(self):
        """Turns off all the lights."""
        pass

    def blink(self, durations):
        """Blinks all lights by turning them on and off for given durations.

        The lights keep blinking indefinitely while the rest of your
        program keeps running.

        This method provides a simple way to make basic but useful patterns.
        For more generic and smooth patterns, use :meth:`.animate` instead.

        Arguments:
            (list): List of (:ref:`time`) values of the
                form ``[on_1, off_1, on_2, off_2, ...]``.
        """

    def animate(self, brightness_values, interval):
        """Animates the lights with a list of brightness tuples. The next
        brightness tuple from the list is activated after the given interval.

        The animation runs in the background while the rest of your program
        keeps running. When the animation completes, it repeats.

        Arguments:
            brightness_values (list): List of :ref:`brightness` tuples.
            interval (:ref:`time`): Time between brightness updates.
        """


class LightMatrix:
    """Control a rectangular grid of single-color lights."""

    def __init__(self, rows, columns):
        """Initializes the light matrix display.

        Arguments:
            rows (int): Number of rows in the grid
            columns (int): Number of columns in the grid
        """
        pass

    def orientation(self, up):
        """Sets the orientation of the light matrix display.

        Only new displayed images and pixels are affected. The existing display
        contents remain unchanged.

        Arguments:
            top (Side): Which side of the light matrix display is "up" in your
                design. Choose ``Side.TOP``, ``Side.LEFT``, ``Side.RIGHT``,
                or ``Side.BOTTOM``.
        """
        pass

    def image(self, matrix):
        """Displays an image, represented by a matrix of :ref:`brightness`
        values.

        Arguments:
            matrix (Matrix): Matrix of intensities (:ref:`brightness`).  A 2D
                list is also accepted.
        """
        pass

    def animate(self, matrices, interval):
        """Displays an animation made using a list of images.

        Each image has the same format as above. Each image is
        shown for the given interval. The animation repeats
        forever while the rest of your program keeps running.

        Arguments:
            matrix (list): List of Matrix of intensities.
            interval (:ref:`time`): Time to display each image in the list.
        """
        pass

    def pixel(self, row, column, brightness=100):
        """Turns on one pixel at the specified brightness.

        Arguments:
            row (int): Vertical grid index, starting at 0 from the top.
            column (int): Horizontal grid index, starting at 0 from the left.
            brightness (:ref:`brightness`): Brightness of the pixel.
        """
        pass

    def off(self):
        """Turns off all the pixels."""
        pass

    def number(self, number):
        """Displays a number in the range -99 to 99.

        A minus sign (``-``) is shown as a faint dot
        in the center of the display. Numbers greater than 99 are
        shown as ``>``. Numbers less than -99 are shown as ``<``.

        Arguments:
            number (int): The number to be displayed.
        """
        pass

    def char(self, char):
        """Displays a character or symbol on the light grid. This may
        be any letter (``a``--``z``), capital letter (``A``--``Z``) or one of
        the following symbols: ``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}``.

        Arguments:
            character (str): The character or symbol to be displayed.
        """
        pass

    def text(self, text, on=500, off=50):
        """Displays a text string, one character at a time, with a pause
        between each character. After the last character is shown, all lights
        turn off.

        Arguments:
            text (str): The text to be displayed.
            on (:ref:`time`): For how long a character is shown.
            off (:ref:`time`): For how long the display is off between
                characters.
        """
        pass

    def reset(self):
        """Resets the display to show the default run animation."""
        pass


class Keypad:
    """Get status of buttons on a keypad layout."""

    def __init__(self, active_buttons):
        pass

    def pressed(self):
        """Checks which buttons are currently pressed.

        :returns: Tuple of pressed buttons.
        :rtype: Tuple of :class:`Button`

        """
        pass


class Battery:
    """Get the status of a battery."""

    def voltage(self):
        """Gets the voltage of the battery.

        Returns:
            :ref:`voltage`: Battery voltage.
        """
        pass

    def current(self):
        """Gets the current supplied by the battery.

        Returns:
            :ref:`current`: Battery current.

        """
        pass


class SimpleAccelerometer:
    """Get measurements from an accelerometer."""

    def acceleration(self):
        """Gets the acceleration of the device.

        Returns:
            tuple of :ref:`linacceleration_m`: Acceleration along all three
            axes.
        """
        pass

    def up(self):
        """Checks which side of the hub currently faces upward.

        :returns:
            ``Side.TOP``, ``Side.BOTTOM``, ``Side.LEFT``, ``Side.RIGHT``,
            ``Side.FRONT`` or ``Side.BACK``.
        :rtype: :class:`Side`

        """
        pass


class Accelerometer(SimpleAccelerometer):
    """Get measurements from an accelerometer."""

    def neutral(self, top, front):
        """Configures the neutral orientation of the device or hub. You do this
        by specifying how it is mounted on your design, in terms of the
        :ref:`robot reference frame <robotframe>`.

        In this given neutral orientation, the tilt and heading will then be
        zero.

        Arguments:
            top (Axis): Which direction the top of the device faces in the
                        neutral orientation. For example, you can
                        choose ``top=-Axis.Z`` if you mounted it such that the
                        neutral orientation is upside down.
            front (Axis): Which direction the front of the device faces in the
                        neutral orientation.
        """
        pass

    def acceleration(self, axis=None):
        """Gets the acceleration of the device along a given axis in the
        :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axis along which the acceleration is
                         measured.
        Returns:
            :ref:`linacceleration_m`: Acceleration along the
            specified axis. If you specify no axis, this returns a vector
            of accelerations along all axes.
        """
        pass

    def tilt(self):
        """Gets the pitch and roll angles. This is relative to the
        :ref:`user-specified neutral orientation <robotframe>`.

        The order of rotation is pitch-then-roll. This is equivalent to a
        positive rotation along the robot y-axis and then a positive rotation
        along the x-axis.

        Returns:
            (:ref:`angle`, :ref:`angle`): Pitch and roll angles.

        """
        pass

    def tapped(self):
        """Checks if the device or hub was tapped.

        Returns:
            bool:
                ``True`` if tapped since this method was last called. ``False``
                otherwise.

        """
        pass

    def shaken(self):
        """Checks if the device or hub was shaken.

        Returns:
            bool:
                ``True`` if shaken since this method was last called. ``False``
                otherwise.

        """
        pass


class IMU(Accelerometer):

    def heading(self):
        """Gets the heading angle relative to the starting orientation. It is a
        a positive rotation around the :ref:`z-axis in the robot
        frame <robotframe>`, prior to applying any tilt rotation.

        For a vehicle viewed from the top, this means that
        a positive heading value corresponds to a counterclockwise rotation.

        .. note:: This method is not yet implemented.

        Returns:
            :ref:`angle`: Heading angle relative to starting orientation.

        """
        pass

    def reset_heading(self, angle):
        """Resets the accumulated heading angle of the robot.

        .. note:: This method is not yet implemented.

        Arguments:
            angle (:ref:`angle`): Value to which the heading should be reset.
        """
        pass

    def angular_velocity(self, axis=None):
        """Gets the angular velocity of the device along a given axis in
        the :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axis along which the angular velocity is
                         measured.
        Returns:
            :ref:`speed`: Angular velocity along the
            specified axis. If you specify no axis, this returns a vector
            of accelerations along all axes.
        """
        pass
