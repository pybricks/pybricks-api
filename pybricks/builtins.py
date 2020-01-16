"""Generic cross-platform module for typical devices like lights, displays,
speakers, and batteries."""

from .parameters import Direction, Stop, Axis


class DCMotor():
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
        """Rotate the motor at a given duty cycle (also known as "power").

        Arguments:
            duty (:ref:`percentage`): The duty cycle (-100.0 to 100).
        """
        pass

    def set_dc_settings(self, duty_limit, duty_offset):
        """Configure the settings to adjust the behavior of the :meth:`.dc`
        command. This also affects all of the ``run`` commands, which use
        the :meth:`.dc` method in the background.

        Arguments:
            duty_limit (:ref:`percentage`): Relative torque limit during
                                            subsequent motor commands. This
                                            sets the maximum duty cycle that is
                                            applied during any subsequent motor
                                            command. This reduces the maximum
                                            torque output to a percentage of
                                            the absolute maximum stall torque.
                                            This is useful to avoid applying
                                            the full motor torque to a geared
                                            or lever mechanism, or to prevent
                                            your LEGO® train from
                                            unintentionally going at full
                                            speed. (*Default*: 100).
            duty_offset (:ref:`percentage`): Minimum duty cycle given when you
                                             use :meth:`.dc`. This adds a small
                                             feed forward torque so that your
                                             motor will move even for very low
                                             duty cycle values, which can be
                                             useful when you create your own
                                             feedback controllers
                                             (*Default*: 0).
        """
        pass


class Motor(DCMotor):
    """Generic class to control motors with built-in rotation sensors."""

    def __init__(self, port,
                 positive_direction=Direction.CLOCKWISE,
                 gears=None):
        """

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive speed value or
                angle (*Default*: ``Direction.CLOCKWISE``).
            gears (list):
                List of gears linked to the motor (*Default*:``None``).

                For example: ``[12, 36]`` represents a gear train with a
                12-tooth and a 36-tooth gear. Use a list of lists for multiple
                gear trains, such as ``[[12, 36], [20, 16, 40]]``.

                When you specify a gear train, all motor commands and settings
                are automatically adjusted to account for the resulting gear
                ratio.  The motor direction remains unchanged by this. See
                :ref:`gears` for more information.
        """
        pass

    def angle(self):
        """Get the rotation angle of the motor.

        Returns:
            :ref:`angle`: Motor angle.

        """
        pass

    def speed(self):
        """Get the speed (angular velocity) of the motor.

        Returns:
            :ref:`speed`: Motor speed.

        """
        pass

    def stalled(self):
        """Check whether the motor is currently stalled.

        A motor is stalled when it cannot move even with the maximum torque.
        For example, when something is blocking the motor or your mechanism
        simply cannot turn any further. See :ref:`stalled` for more
        information.

        Returns:
            bool: ``True`` if the motor is stalled, ``False`` if it is not.

        """
        pass

    def reset_angle(self, angle):
        """Reset the accumulated rotation angle of the motor.

        Arguments:
            angle (:ref:`angle`): Value to which the angle should be reset. If
                                  you don't specify an angle, the absolute
                                  value will be used if the motor supports it.
        """
        pass

    def stop(self, stop_type=Stop.COAST):
        """Stop the motor.

        Arguments:
            stop_type (Stop): Whether to coast, brake, or hold (*Default*:
                              :class:`Stop.COAST <.parameters.Stop>`).
        """
        pass

    def run(self, speed):
        """Keep the motor running at a constant speed (angular velocity).

        The motor will accelerate towards the requested speed and the duty
        cycle is automatically adjusted to keep the speed constant, even under
        some load. This continues in the background until you give the motor a
        new command or the program stops.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
        """
        pass

    def run_time(self, speed, time, stop_type=Stop.COAST, wait=True):
        """Run the motor at a constant speed (angular velocity) for a given
        amount of time.

        The motor will accelerate towards the requested speed and the duty
        cycle is automatically adjusted to keep the speed constant, even under
        some load. It begins to decelerate just in time to reach standstill
        after the specified duration.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            time (:ref:`time`): Duration of the maneuver.
            stop_type (Stop): Whether to coast, brake, or hold after coming to
                              a standstill (*Default*:
                              :class:`Stop.COAST <.parameters.Stop>`).
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program (*Default*: ``True``).
                         This means that your program waits for the
                         specified ``time``.
        """
        pass

    def run_angle(self, speed, rotation_angle,
                  stop_type=Stop.COAST, wait=True):
        """Run the motor at a constant speed (angular velocity) by a given
        angle.

        The motor will accelerate towards the requested speed and the duty
        cycle is automatically adjusted to keep the speed constant, even under
        some load. It begins to decelerate just in time so that it comes to a
        standstill after traversing the given angle.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            rotation_angle (:ref:`angle`): Angle by which the motor should
                                           rotate.
            stop_type (Stop): Whether to coast, brake, or hold after coming to
                              a standstill (*Default*:
                              :class:`Stop.COAST <.parameters.Stop>`).
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program (*Default*: ``True``).
                         This means that your program waits until the motor has
                         traveled precisely the requested angle.
        """
        pass

    def run_target(self, speed, target_angle, stop_type=Stop.COAST, wait=True):
        """ Run the motor at a constant speed (angular velocity) towards a
        given target angle.

        The motor will accelerate towards the requested speed and the duty
        cycle is automatically adjusted to keep the speed constant, even under
        some load. It begins to decelerate just in time so that it comes to a
        standstill at the given target angle.

        The direction of rotation is automatically selected based on the target
        angle.

        Arguments:
            speed (:ref:`speed`): Absolute speed of the motor. The direction
                                  will be automatically selected based on the
                                  target angle: it makes no difference if you
                                  specify a positive or negative speed.
            target_angle (:ref:`angle`): Target angle that the motor should
                                         rotate to, regardless of its current
                                         angle.
            stop_type (Stop): Whether to coast, brake, or hold after coming to
                              a standstill (*Default*:
                              :class:`Stop.COAST <.parameters.Stop>`).
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program (*Default*: ``True``).
                         This means that your program waits until the motor
                         has reached the target angle.
        """
        pass

    def run_until_stalled(self, speed, stop_type=Stop.COAST, duty_limit=None):
        """Run the motor at a constant speed (angular velocity) until it
        stalls. The motor is considered stalled when it cannot move even with
        the maximum torque. See :meth:`.stalled` for a more precise definition.

        The ``duty_limit`` argument lets you temporarily limit the motor torque
        during this maneuver. This is useful to avoid applying the full motor
        torque to a geared or lever mechanism.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            stop_type (Stop): Whether to coast, brake, or hold after coming to
                              a standstill (*Default*:
                              :class:`Stop.COAST <.parameters.Stop>`).
            duty_limit (:ref:`percentage`): Relative torque limit. This limit
                                            works just like
                                            :meth:`.set_dc_settings`, but in
                                            this case the limit is temporary:
                                            it returns to its previous value
                                            after completing this command.
        """
        pass

    def track_target(self, target_angle):
        """Track a target angle that varies in time.

        This function is quite similar to :meth:`.run_target`, but speed and
        acceleration settings are ignored: it will move to the target angle as
        fast as possible. Instead, you adjust speed and acceleration by
        choosing how fast or slow you vary the ``target_angle``.

        This method is useful in fast loops where the motor target changes
        continuously.

        Arguments:
            target_angle (:ref:`angle`): Target angle that the motor should
                                         rotate to.

        """
        pass

    def set_run_settings(self, max_speed, acceleration):
        """Configure the maximum speed and acceleration/deceleration of the
        motor for all run commands.

        This applies to the ``run``, ``run_time``, ``run_angle``,
        ``run_target``, or ``run_until_stalled`` commands you give the motor.

        Arguments:
            max_speed (:ref:`speed`): Maximum speed of the motor during a motor
                                      command.
            acceleration (:ref:`acceleration`): Acceleration towards the target
                                                speed and deceleration towards
                                                standstill. This should be a
                                                positive value. The motor will
                                                automatically change the sign
                                                to decelerate as needed.

        """
        pass

    def set_pid_settings(self, kp, ki, kd, tight_loop_limit, angle_tolerance,
                         speed_tolerance, stall_speed, stall_time):
        """Configure the settings of the position and speed controllers.

        Arguments:
            kp (int): Proportional position (and integral speed) control
                      constant.
            ki (int): Integral position control constant.
            kd (int): Derivative position (and proportional speed) control\
                      constant.
            tight_loop_limit (:ref:`time`): If you execute any of the ``run``
                                            commands within this interval after
                                            starting the previous command, the
                                            controllers assume that you want to
                                            control the speed directly. This
                                            means that it will ignore the
                                            acceleration setting and
                                            immediately begin tracking the
                                            speed you give in the ``run``
                                            command. This is useful in a fast
                                            loop, where you usually want the
                                            motors to respond quickly rather
                                            than accelerate smoothly, for
                                            example with a line-following
                                            robot.
            angle_tolerance (:ref:`angle`): Allowed deviation from the target
                                            angle before motion is considered
                                            complete.
            speed_tolerance (:ref:`speed`): Allowed deviation from zero speed
                                            before motion is considered
                                            complete.
            stall_speed (:ref:`speed`): See :meth:`.stalled`.
            stall_time (:ref:`time`): See :meth:`.stalled`.
        """
        pass


class Speaker():
    """Play beeps and sounds using a speaker."""

    def beep(self, frequency=500, duration=100):
        """Play a beep/tone.

        Arguments:
            frequency (:ref:`frequency`):
                Frequency of the beep (*Default*: 500). Frequencies below 100
                are treated as 100.
            duration (:ref:`time`):
                Duration of the beep (*Default*: 100). If the duration is less
                than 0, then the method returns immediately and the frequency
                play continues to play indefinitely.
        """
        pass

    def play_notes(self, notes, tempo=120):
        """Play a sequence of notes.

        Notes are strings with the following format:

        - The first character is the name of the note, ``A`` to ``G`` or ``R``
          for a rest.
        - Note names can also include an accidental ``#`` (sharp) or ``b``
          (flat). ``B#``/``Cb`` and ``E#``/``Fb`` are not allowed.
        - The note name is followed by the octave number ``2`` to ``8``. For
          example ``C4`` is middle C. The octave changes to the next number at
          the note C, for example, ``B3`` is the note below middle C (``C4``).
        - The octave is followed by ``/`` and a number that indicates the size
          of the note. For example ``/4`` is a quarter note, ``/8`` is an
          eight note and so on.
        - This can optionally followed by a ``.`` to make a dotted note.
          Dotted notes are 1-1/2 times as long as notes without a dot.
        - The note can optionally end with a ``_`` which is a tie or a slur.
          This causes there to be no pause between this note and the next note.

        Arguments:
            notes (iter):
                A sequence of notes to be played (see format above).
            tempo (int):
                Beats per minute where a quarter note is one beat.
        """
        pass

    def play_file(self, file_name):
        """Play a sound file.

        Arguments:
            file_name (str):
                Path to the sound file, including the file extension.
        """

        pass

    def say(self, text):
        """Say a given text string.

        You can configure the language and voice of the text using
        :meth:`set_speech_options`.

        Arguments:
            text (str): What to say.
        """

        pass

    def set_speech_options(self, language=None, voice=None, speed=None, pitch=None):
        """Configure speech settings used by the :meth:`say` method.

        Any option that is set to ``None`` will not be changed. If an option
        is set to an invalid value :meth:`say` will use the default value
        instead.

        Arguments:
            language (str):
                Language of the text. For example, you can choose ``'en'``
                (English) or ``'de'`` (German). A list of all available
                languages is given below.
            voice (str):
                The voice to use. For example, you can choose ``'f1'`` (female
                voice variant 1) or ``'m3'`` (male voice variant 3). A list of
                all available voices is given below.
            speed (int):
                Number of words per minute.
            pitch (int):
                Pitch (0 to 99). Higher numbers make the voice higher pitched
                and lower numbers make the voice lower pitched.
        """
        pass

    def set_volume(self, volume, which='_all_'):
        """Set the speaker volume.

        Arguments:
            volume (:ref:`percentage`):
                Volume of the speaker.
            which (str):
                The specific volume to set. Can be ``Beep``, ``PCM`` or
                ``_all_``. ``Beep`` controls the volume for :meth:`beep` and
                :meth:`play_notes`. ``PCM`` controls the volume for
                :meth:`play_file` and :meth:`say`. ``_all_`` sets both at the
                same time.
        """
        pass


class Light():
    """Control a single-color light."""

    def on(self, brightness=100):
        """Turn on the light at the specified brightness.

        Arguments:
            brightness (:ref:`brightness`):
                Brightness of the light (*Default*: 100).
        """

    def off(self):
        """Turn off the light."""
        pass


class ColorLight():
    """Control a multi-color light."""

    def on(self, color):
        """Turn on the light at the specified color and brightness.

        Arguments:
            color (Color): Color of the light. The light turns off if you
                           choose ``None`` or a color that is not available.
        """
        pass

    def off(self):
        """Turn off the light."""
        pass

    def rgb(self, red, green, blue):
        """Set the brightness of the red, green, and blue light.

        Arguments:
            red (:ref:`brightness`): Brightness of the red light.
            green (:ref:`brightness`): Brightness of the green light.
            blue (:ref:`brightness`): Brightness of the blue light.
        """
        pass


class LightArray():
    """Control an array of single-color lights."""

    def __init__(self, lights):
        """Initialize the light array.

        Arguments:
            lights (int): Number of lights
        """
        pass

    def on(self, brightness=100):
        """Turn on all the lights at the specified brightness.

        Arguments:
            brightness (:ref:`brightness`):
                Brightness of the lights (*Default*: 100).
        """
        pass

    def off(self):
        """Turn off all the lights."""
        pass

    def array(self, *brightnesses):
        """array(first_light, ..., last_light)

        Set the brightness of each light individually.

        Arguments:
            brightness (:ref:`brightness`, ..., :ref:`brightness`):
                Brightness of each light.
        """
        pass


class LightGrid():
    """Control a rectangular grid of single-color lights."""

    def __init__(self, rows, columns):
        """Initialize the light grid.

        Arguments:
            rows (int): Number of rows in the grid
            columns (int): Number of columns in the grid
        """
        pass

    def image(self, matrix, clear=True):
        """Show an image made up of pixels of a given brightness.

        Arguments:
            matrix (2D Array): Matrix of intensities (:ref:`brightness`).
            clear (bool): Whether to turn off all the lights before showing
                the new image (*Default*: ``True``). If you choose ``False``,
                the given matrix is added to one already shown.
        """
        pass

    def pixel(self, row, column, brightness):
        """Turn on a pixel at the specified brightness.

        Arguments:
            row (int): Vertical grid index, starting at 0 from the top.
            column (int): Horizontal grid index, starting at 0 from the left.
            brightness (:ref:`brightness`): Brightness of the pixel.
        """
        pass

    def on(self, brightness=100):
        """Turn on all the pixels at the specified brightness.

        Arguments:
            brightness (:ref:`brightness`):
                Brightness of the lights (*Default*: 100).
        """
        pass

    def off(self):
        """Turn off all the pixels."""
        pass

    def number(self, number):
        """Display a number on the light grid.

        Arguments:
            number (int): The number to be displayed.
        """
        pass

    def char(self, character):
        """Display a character or symbol on the light grid. This may
        be any letter (``a``--``z``), capital letter (``A``--``Z``) or one of
        the following symbols: ``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}``.

        Arguments:
            character (str): The character or symbol to be displayed.
        """
        pass

    def text(self, text, pause=500):
        """Display a text string, one character at a time, with a pause
        between each character. After the last character is shown, the light
        grid turns off.

        Arguments:
            character (str): The character or symbol to be displayed.
            time (:ref:`time`): How long to show a character before showing
                                the next one.
        """
        pass


class KeyPad():
    """Get status of buttons on a keypad layout."""

    def pressed(self):
        """Check which buttons are currently pressed.

        :returns: List of pressed buttons.
        :rtype: List of :class:`Button <.parameters.Button>`

        """
        pass


class Battery():
    """Get the status of a battery."""

    def voltage(self):
        """Get the voltage of the battery.

        Returns:
            :ref:`voltage`: Battery voltage.
        """
        pass

    def current(self):
        """Get the current supplied by the battery.

        Returns:
            :ref:`current`: Battery current.

        """
        pass


class Accelerometer():
    """Get measurements from an accelerometer."""

    def neutral(self, top, front):
        """Configure the neutral orientation of the device or hub. You do this
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

    def acceleration(self, axis=Axis.ALL):
        """acceleration(axis=Axis.ALL)

        Measure the acceleration of the device along a given axis in the
        :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axis along which the acceleration is
                         measured. (*Default*: ``axis=Axis.ALL``)
        Returns:
            :ref:`linacceleration`. Returns a :ref:`scalar` of the acceleration
            along the specified axis.
            If you choose ``axis=Axis.ALL``, you get a :ref:`vector` with the
            accelerations along all three axes (x, y, z).

        """
        pass

    def tilt(self):
        """Get the pitch and roll angles relative to the neutral, horizontal
        orientation.

        The order of rotation is pitch-then-roll. This is equivalent to a
        positive rotation along the x-axis and then a positive rotation
        along the y-axis.

        Returns:
            (:ref:`angle`, :ref:`angle`): Pitch and roll angles.

        """
        pass

    def tapped(self):
        """Check if the device or hub was tapped.

        Returns:
            bool:
                ``True`` if tapped since this method was last called. ``False``
                otherwise.

        """
        # def tapped(self, axis=Axis.ALL, bidirectional=True, tolerance=45):
        pass

    def shaken(self):
        """Check if the device or hub was shaken.

        Returns:
            bool:
                ``True`` if shaken since this method was last called. ``False``
                otherwise.

        """
        # def shaken(self, axis=Axis.ALL, bidirectional=True, tolerance=45):
        pass

    def up(self):
        """Check which side of the device or hub currently faces upward.

        :returns:
            ``Side.TOP``, ``Side.BOTTOM``, ``Side.LEFT``, ``Side.RIGHT``,
            ``Side.FRONT`` or ``Side.BACK``.
        :rtype: :class:`Side <.parameters.Side>`

        """
        pass


class IMU(Accelerometer):

    def heading(self):
        """Get the heading angle relative to the starting orientation. It is a
        a positive rotation around the :ref:`z-axis in the robot
        frame <robotframe>`, prior to applying any tilt rotation.

        For a vehicle viewed from the top, this means that
        a positive heading value corresponds to a counterclockwise rotation.

        Returns:
            :ref:`angle`: Heading angle relative to starting orientation.

        """
        pass

    def reset_heading(self, angle):
        """Reset the accumulated heading angle of the robot.

        Arguments:
            angle (:ref:`angle`): Value to which the heading should be reset.
        """
        pass

    def gyro(self, axis=Axis.ALL):
        """gyro(axis=Axis.ALL)

        Measure the angular velocity of the device along a given axis in the
        :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axis along which the angular velocity is
                         measured. (*Default*: ``axis=Axis.ALL``)
        Returns:
            :ref:`speed`. Returns a :ref:`scalar` of the angular velocity
            along the specified axis.
            If you choose ``axis=Axis.ALL``, you get a :ref:`vector` with the
            angular velocities along all three axes (x, y, z).

        """
        pass
