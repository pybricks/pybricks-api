# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

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

    def limits(self, speed, acceleration, actuation):
        """Configures the maximum speed, acceleration, and actuation.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (:ref:`speed` or :ref:`linspeed`):
                Maximum speed. All speed commands will be capped to this value.
            acceleration (:ref:`acceleration` or :ref:`linacceleration`):
                Maximum acceleration.
            actuation (:ref:`percentage`):
                Maximum actuation as percentage of absolute maximum.
        """
        pass

    def pid(self, kp, ki, kd, integral_range, integral_rate, feed_forward):
        """Gets or sets the PID values for position and speed control.

        If no arguments are given, this will return the current values.

        Arguments:
            kp (int): Proportional position (or integral speed) control
                constant.
            ki (int): Integral position control constant.
            kd (int): Derivative position (or proportional speed) control
                constant.
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
        angle. It does matter if ``speed`` is positive or negative.

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
            duty_limit (:ref:`percentage`): Torque limit during this
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
        """Plays a sequence of musical notes.

        For example, you can play: ``['C4/4', 'C4/4', 'G4/4', 'G4/4']``.

        Arguments:
            notes (iter):
                A sequence of notes to be played (see format below).
            tempo (int):
                Beats per minute where a quarter note is one beat.
        """
        pass

    def play_file(self, file_name):
        """Plays a sound file.

        Arguments:
            file_name (str):
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


class ColorLight:
    """Control a multi-color light."""

    def on(self, color):
        """Turns on the light at the specified color.

        Arguments:
            color (Color): Color of the light. The light turns off if you
                           choose ``None`` or a color that is not available.
        """
        pass

    def off(self):
        """Turns off the light."""
        pass

    def rgb(self, red, green, blue):
        """Sets the brightness of the red, green, and blue light.

        Arguments:
            red (:ref:`brightness`): Brightness of the red light.
            green (:ref:`brightness`): Brightness of the green light.
            blue (:ref:`brightness`): Brightness of the blue light.
        """
        pass


class KeyPad:
    """Get status of buttons on a keypad layout."""

    def pressed(self):
        """Checks which buttons are currently pressed.

        :returns: List of pressed buttons.
        :rtype: List of :class:`Button <.parameters.Button>`

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
