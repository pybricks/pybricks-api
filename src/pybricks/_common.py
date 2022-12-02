# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 The Pybricks Authors

"""Generic cross-platform module for typical devices like lights, displays,
speakers, and batteries."""

from __future__ import annotations

from typing import Union, Iterable, overload, Optional, Tuple, Collection, TYPE_CHECKING

from .geometry import Matrix, Axis
from .parameters import Direction, Stop, Button, Port, Color, Side

if TYPE_CHECKING:
    from .parameters import Number


class System:
    """System control actions for a hub."""

    def set_stop_button(
        self, button: Optional[Union[Button, Iterable[Button]]]
    ) -> None:
        """
        set_stop_button(button)

        Sets the button or button combination that stops a running script.

        Normally, the center button is used to stop a running script. You can
        change or disable this behavior in order to use the button for other
        purposes.

        Arguments:
            button (Button): A button such
                as :attr:`Button.CENTER <pybricks.parameters.Button.CENTER>`,
                or a tuple of multiple buttons. Choose ``None`` to disable the
                stop button altogether.
        """

    def shutdown(self) -> None:
        """shutdown()

        Stops your program and shuts the hub down."""

    def reset_reason(self) -> int:
        """reset_reason() -> int

        Finds out how and why the hub (re)booted. This can be useful to
        diagnose some problems.

        Returns:
            * ``0`` if the hub was previously powered off
              normally.
            * ``1`` if the hub rebooted automatically, like
              after a firmware update.
            * ``2`` if the hub previously
              crashed due to a watchdog timeout, which indicates a firmware
              issue.
        """

    def name(self) -> str:
        """name() -> str

        Gets the hub name. This is the name you see when connecting
        via Bluetooth.

        Returns:
            The hub name.
        """

    @overload
    def storage(self, offset: int, *, read: int) -> bytes:
        ...

    @overload
    def storage(self, offset: int, *, write: bytes) -> None:
        ...

    def storage(self, offset, read=None, write=None):
        """
        storage(self, offset, write=)
        storage(self, offset, read=) -> bytes

        Reads or writes binary data to persistent storage.

        This lets you store data that can be used the next time you run the
        program.

        The data will be saved to flash memory when you turn the hub off
        normally. It will not be saved if the batteries are removed *while* the
        hub is still running.

        Once saved, the data will remain available even after you remove the
        batteries.

        Args:
            offset (int): The offset from the start of the user storage memory, in bytes.
            read (int): The number of bytes to read. Omit this argument when writing.
            write (bytes): The bytes to write. Omit this argument when reading.

        Returns:
            The bytes read if reading, otherwise ``None``.

        Raises:
            ValueError:
                If you try to read or write data outside of the allowed range.
        """


class DCMotor:
    """Generic class to control simple motors without rotation sensors, such
    as train motors."""

    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive duty cycle value.
        """

    def dc(self, duty: Number) -> None:
        """dc(duty)

        Rotates the motor at a given duty cycle (also known as "power").

        Arguments:
            duty (Number, %): The duty cycle (-100.0 to 100).
        """

    def stop(self) -> None:
        """stop()

        Stops the motor and lets it spin freely.

        The motor gradually stops due to friction."""

    def brake(self) -> None:
        """brake()

        Passively brakes the motor.

        The motor stops due to friction, plus the voltage that
        is generated while the motor is still moving."""

    @overload
    def settings(self, max_voltage: Number) -> None:
        ...

    @overload
    def settings(self) -> Tuple[int]:
        ...

    def settings(self, *args):
        """
        settings(max_voltage)
        settings() -> Tuple[int]

        Configures motor settings. If no arguments are given,
        this returns the current values.

        Arguments:
            max_voltage (Number, mV):
                Maximum voltage applied to the motor during all motor commands.
        """


class Control:
    """Class to interact with PID controller and settings."""

    scale: int

    """
    Scaling factor between the controlled integer variable
    and the physical output. For example, for a single
    motor this is the number of encoder pulses per degree of rotation.
    """

    @overload
    def limits(
        self,
        speed: Optional[Number] = None,
        acceleration: Optional[Number] = None,
        torque: Optional[Number] = None,
    ) -> None:
        ...

    @overload
    def limits(self) -> Tuple[int, int, int]:
        ...

    def limits(self, *args):
        """
        limits(speed, acceleration, torque)
        limits() -> Tuple[int, int, int]

        Configures the maximum speed, acceleration, and torque.

        If no arguments are given, this will return the current values.

        The new ``acceleration`` and ``speed`` limit will become effective
        when you give a new motor command. Ongoing maneuvers are not affected.

        Arguments:
            speed (Number, deg/s or Number, mm/s):
                Maximum speed. All speed commands will be capped to this value.
            acceleration (Number, deg/s² or Number, mm/s²):
                Slope of the speed curve when accelerating or decelerating.
                Use a tuple to set acceleration and deceleration separately.
                If one value is given, it is used for both.
            torque (:ref:`torque`):
                Maximum feedback torque during control.
        """

    @overload
    def pid(
        self,
        kp: Optional[Number] = None,
        ki: Optional[Number] = None,
        kd: Optional[Number] = None,
        reserved: Optional[Number] = None,
        integral_rate: Optional[Number] = None,
    ) -> None:
        ...

    @overload
    def pid(self) -> Tuple[int, int, int, None, int]:
        ...

    def pid(self, *args):
        """pid(kp, ki, kd, reserved, integral_rate)
        pid() -> Tuple[int, int, int, None, int]

        Gets or sets the PID values for position and speed control.

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
            reserved: This setting is not used.
            integral_rate (Number, deg/s or Number, mm/s): Maximum rate at
                which the error integral is allowed to grow.
        """

    @overload
    def target_tolerances(
        self, speed: Optional[Number] = None, position: Optional[Number] = None
    ) -> None:
        ...

    @overload
    def target_tolerances(self) -> Tuple[int, int]:
        ...

    def target_tolerances(self, *args):
        """target_tolerances(speed, position)
        target_tolerances() -> Tuple[int, int]

        Gets or sets the tolerances that say when a maneuver is done.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (Number, deg/s or Number, mm/s): Allowed deviation
                from zero speed before motion is considered complete.
            position (Number, deg or :ref:`distance`): Allowed
                deviation from the target before motion is considered
                complete.
        """

    @overload
    def stall_tolerances(
        self, speed: Optional[Number] = None, time: Optional[Number] = None
    ) -> None:
        ...

    @overload
    def stall_tolerances(self) -> Tuple[int, int]:
        ...

    def stall_tolerances(self, speed, time):
        """stall_tolerances(speed, time)
        stall_tolerances() -> Tuple[int, int]

        Gets or sets stalling tolerances.

        If no arguments are given, this will return the current values.

        Arguments:
            speed (Number, deg/s or Number, mm/s): If the controller
                cannot reach this speed for some ``time`` even with maximum
                actuation, it is stalled.
            time (Number, ms): How long the controller has to be below this
                minimum ``speed`` before we say it is stalled.
        """


class Motor(DCMotor):
    """Generic class to control motors with built-in rotation sensors."""

    control = Control()
    """The motors use PID control to accurately track the speed and
    angle targets that you specify. You can change its behavior through the
    ``control`` attribute of the motor. See :ref:`control` for an overview
    of available methods."""

    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None,
        reset_angle: bool = True,
    ):
        """__init__(port, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True)

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
            reset_angle(bool):
                Choose ``True`` to reset the rotation sensor value to the
                absolute marker angle (between -180 and 179).
                Choose ``False`` to keep the
                current value, so your program knows where it left off last
                time.
        """

    def angle(self) -> int:
        """angle() -> int: deg

        Gets the rotation angle of the motor.

        Returns:
            Motor angle.
        """

    def speed(self) -> int:
        """speed() -> int: deg/s

        Gets the speed of the motor.

        Returns:
            Motor speed.

        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Checks if the motor is currently stalled.

        It is stalled when it cannot reach the target speed or position, even
        with the maximum actuation signal.

        Returns:
            ``True`` if the motor is stalled, ``False`` if not.
        """

    def load(self) -> int:
        """load() -> int: mNm

        Estimates the load that holds back the motor when it tries to move.

        Returns:
            The load torque.
        """

    def reset_angle(self, angle: Optional[Number]) -> None:
        """
        reset_angle(angle)

        Sets the accumulated rotation angle of the motor to a desired value.

        Arguments:
            angle (Number, deg): Value to which the angle should be reset.
        """

    def hold(self) -> None:
        """hold()

        Stops the motor and actively holds it at its current angle."""

    def run(self, speed: Number) -> None:
        """run(speed)

        Runs the motor at a constant speed.

        The motor accelerates to the given speed and keeps running at this
        speed until you give a new command.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
        """

    def run_time(
        self, speed: Number, time: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> None:
        """run_time(speed, time, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed for a given amount of time.

        The motor accelerates to the given speed, keeps running at this speed,
        and then decelerates. The total maneuver lasts for exactly the given
        amount of ``time``.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            time (Number, ms): Duration of the maneuver.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                with the rest of the program.
        """

    def run_angle(
        self,
        speed: Number,
        rotation_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> None:
        """run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed by a given angle.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            rotation_angle (Number, deg): Angle by which the motor should
                rotate.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                with the rest of the program.
        """

    def run_target(
        self,
        speed: Number,
        target_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> None:
        """run_target(speed, target_angle, then=Stop.HOLD, wait=True)

        Runs the motor at a constant speed towards a given target angle.

        The direction of rotation is automatically selected based on the target
        angle. It does not matter if ``speed`` is positive or negative.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            target_angle (Number, deg): Angle that the motor should rotate to.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the motor to reach the target
                before continuing with the rest of the program.
        """

    def run_until_stalled(
        self,
        speed: Number,
        then: Stop = Stop.COAST,
        duty_limit: Optional[Number] = None,
    ) -> int:
        """
        run_until_stalled(speed, then=Stop.COAST, duty_limit=None) -> int: deg

        Runs the motor at a constant speed until it stalls.

        Arguments:
            speed (Number, deg/s): Speed of the motor.
            then (Stop): What to do after coming to a standstill.
            duty_limit (Number, %): Duty cycle limit during this
                command. This is useful to avoid applying the full motor
                torque to a geared or lever mechanism. If it is ``None``, the
                duty limit won't be changed during this command.

        Returns:
            Angle at which the motor becomes stalled.
        """

    def done(self) -> bool:
        """done() -> bool

        Checks if an ongoing command or maneuver is done.

        Returns:
            ``True`` if the command is done, ``False`` if not.
        """

    def track_target(self, target_angle: Number) -> None:
        """track_target(target_angle)

        Tracks a target angle. This is similar to :meth:`.run_target`, but
        the usual smooth acceleration is skipped: it will move to the target
        angle as fast as possible. This method is useful if you want to
        continuously change the target angle.

        Arguments:
            target_angle (Number, deg): Target angle that the motor should
                rotate to.
        """


class Speaker:
    """Plays beeps and sounds using a speaker."""

    @overload
    def volume(self, volume: Number) -> None:
        ...

    @overload
    def volume(self) -> int:
        ...

    def volume(self, *args):
        """volume(volume)
        volume() -> int: %

        Gets or sets the speaker volume.

        If no volume is given, this method returns the current volume.

        Arguments:
            volume (Number, %): Volume of the speaker in the 0-100 range.
        """

    def beep(self, frequency: Number = 500, duration: Number = 100) -> None:
        """beep(frequency=500, duration=100)

        Play a beep/tone.

        Arguments:
            frequency (Number, Hz):
                Frequency of the beep in the 64-24000 Hz range.
            duration (Number, ms):
                Duration of the beep. If the duration is less
                than 0, then the method returns immediately and the frequency
                play continues to play indefinitely.
        """

    def play_notes(self, notes: Iterable[str], tempo: Number = 120) -> None:
        """play_notes(notes, tempo=120)

        Plays a sequence of musical notes. For example:
        ``["C4/4", "C4/4", "G4/4", "G4/4"]``.

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


class ColorLight:
    """Control a multi-color light."""

    def on(self, color: Color) -> None:
        """on(color)

        Turns on the light at the specified color.

        Arguments:
            color (Color): Color of the light.
        """

    def off(self) -> None:
        """off()

        Turns off the light."""

    def blink(self, color: Color, durations: Collection[Number]) -> None:
        """blink(color, durations)

        Blinks the light at a given color by turning it on and off for given
        durations.

        The light keeps blinking indefinitely while the rest of your
        program keeps running.

        This method provides a simple way to make basic but useful patterns.
        For more generic and multi-color patterns, use ``animate()``
        instead.

        Arguments:
            color (Color): Color of the light.
            durations (list): Sequence of time values of the
                form ``[on_1, off_1, on_2, off_2, ...]``.
        """

    def animate(self, colors: Collection[Color], interval: Number) -> None:
        """animate(colors, interval)

        Animates the light with a sequence of colors, shown one by
        one for the given interval.

        The animation runs in the background while the rest of your program
        keeps running. When the animation completes, it repeats.

        Arguments:
            colors (list): Sequence of :class:`Color <.parameters.Color>`
                values.
            interval (Number, ms): Time between color updates.
        """


class LightArray3:
    """Control an array of three single-color lights."""

    def on(self, brightness: Union[Number, Tuple[Number, Number, Number]]) -> None:
        """on(brightness)

        Turns on the lights at the specified brightness.

        Arguments:
            brightness (Number or tuple, %):
                Use a single value to set the brightness of all lights at the
                same time. Use a tuple of three values to set the brightness
                of each light individually.
        """

    def off(self) -> None:
        """off()

        Turns off all the lights."""


class LightArray4(LightArray3):
    """Control an array of four single-color lights."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number, Number]]
    ) -> None:
        """on(brightness)

        Turns on the lights at the specified brightness.

        Arguments:
            brightness (Number or tuple, %):
                Use a single value to set the brightness of all lights at the
                same time. Use a tuple of four values to set the brightness
                of each light individually. The order of the lights is shown
                in the image above.
        """


class LightMatrix:
    """Control a rectangular grid of single-color lights."""

    def __init__(self, rows: int, columns: int):
        """LightMatrix(rows, columns)

        Initializes the light matrix display.

        Arguments:
            rows (int): Number of rows in the grid
            columns (int): Number of columns in the grid
        """

    def orientation(self, up: Side) -> None:
        """orientation(up)

        Sets the orientation of the light matrix display.

        Only new displayed images and pixels are affected. The existing display
        contents remain unchanged.

        Arguments:
            top (Side): Which side of the light matrix display is "up" in your
                design. Choose ``Side.TOP``, ``Side.LEFT``, ``Side.RIGHT``,
                or ``Side.BOTTOM``.
        """

    def icon(self, icon: Matrix) -> None:
        """icon(icon)

        Displays an icon, represented by a matrix of :ref:`brightness`
        values.

        Arguments:
            icon (Matrix): Matrix of intensities (:ref:`brightness`). A 2D
                list is also accepted.
        """

    def animate(self, matrices: Collection[Matrix], interval: Number) -> None:
        """animate(matrices, interval)

        Displays an animation made using a list of images.

        Each image has the same format as above. Each image is
        shown for the given interval. The animation repeats
        forever while the rest of your program keeps running.

        Arguments:
            matrices (iter): Sequence of
                :class:`Matrix <pybricks.geometry.Matrix>` of intensities.
            interval (Number, ms): Time to display each image in the list.
        """

    def pixel(self, row: Number, column: Number, brightness: Number = 100) -> None:
        """pixel(row, column, brightness=100)

        Turns on one pixel at the specified brightness.

        Arguments:
            row (Number): Vertical grid index, starting at 0 from the top.
            column (Number): Horizontal grid index, starting at 0 from the left.
            brightness (Number :ref:`brightness`): Brightness of the pixel.
        """

    def off(self) -> None:
        """off()

        Turns off all the pixels."""

    def number(self, number: Number) -> None:
        """number(number)

        Displays a number in the range -99 to 99.

        A minus sign (``-``) is shown as a faint dot
        in the center of the display. Numbers greater than 99 are
        shown as ``>``. Numbers less than -99 are shown as ``<``.

        Arguments:
            number (int): The number to be displayed.
        """

    def char(self, char: str) -> None:
        """char(char)

        Displays a character or symbol on the light grid. This may
        be any letter (``a``--``z``), capital letter (``A``--``Z``) or one of
        the following symbols: ``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}``.

        Arguments:
            character (str): The character or symbol to be displayed.
        """

    def text(self, text: str, on: Number = 500, off: Number = 50) -> None:
        """text(text, on=500, off=50)

        Displays a text string, one character at a time, with a pause
        between each character. After the last character is shown, all lights
        turn off.

        Arguments:
            text (str): The text to be displayed.
            on (Number, ms): For how long a character is shown.
            off (Number, ms): For how long the display is off between
                characters.
        """


class Keypad:
    """Get status of buttons on a keypad layout."""

    def __init__(self, active_buttons):
        ...

    def pressed(self) -> Collection[Button]:
        """pressed() -> Collection[Button]

        Checks which buttons are currently pressed.

        Returns:
            Set of pressed buttons.
        """


class Battery:
    """Get the status of a battery."""

    def voltage(self) -> int:
        """voltage() -> int: mV

        Gets the voltage of the battery.

        Returns:
            Battery voltage.
        """

    def current(self) -> int:
        """current() -> int: mA

        Gets the current supplied by the battery.

        Returns:
            Battery current.
        """


class Charger:
    """Get the status of a battery charger."""

    def connected(self) -> bool:
        """connected() -> bool

        Checks whether a charger is connected via USB.

        Returns:
            ``True`` if a charger is connected, ``False`` if not.
        """

    def status(self) -> int:
        """status() -> int

        Gets the status of the battery charger, represented by one of the
        following values. This corresponds to the battery light indicator
        right next to the USB port.

            0. Not charging (light is off).
            1. Charging (light is red).
            2. Charging is complete (light is green).
            3. There is a problem with the charger (light is yellow).

        Returns:
            Status value.
        """

    def current(self) -> int:
        """current() -> int: mA

        Gets the charging current.

        Returns:
            Charging current.
        """


class SimpleAccelerometer:
    """Get measurements from an accelerometer."""

    def acceleration(self) -> Tuple[int, int, int]:
        """acceleration() -> Tuple[int, int, int]: mm/s²

        Gets the acceleration of the device.

        Returns:
            Acceleration along all three axes.
        """

    def up(self) -> Side:
        """up() -> Side

        Checks which side of the hub currently faces upward.

        Returns:
            ``Side.TOP``, ``Side.BOTTOM``, ``Side.LEFT``, ``Side.RIGHT``,
            ``Side.FRONT`` or ``Side.BACK``.
        """


class Accelerometer(SimpleAccelerometer):
    """Get measurements from an accelerometer."""

    @overload
    def acceleration(self, axis: Axis) -> float:
        ...

    @overload
    def acceleration(self) -> Matrix:
        ...

    def acceleration(self, *args):
        """
        acceleration(axis) -> float: mm/s²
        acceleration() -> vector: mm/s²


        Gets the acceleration of the device along a given axis in the
        :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axis along which the acceleration should be
                         measured.
        Returns:
            Acceleration along the specified axis. If you specify no axis,
            this returns a vector of accelerations along all axes.
        """

    def tilt(self) -> Tuple[int, int]:
        """tilt() -> Tuple[int, int]

        Gets the pitch and roll angles. This is relative to the
        :ref:`user-specified neutral orientation <robotframe>`.

        The order of rotation is pitch-then-roll. This is equivalent to a
        positive rotation along the robot y-axis and then a positive rotation
        along the x-axis.

        Returns:
            Tuple of pitch and roll angles.
        """


class IMU(Accelerometer):
    def heading(self) -> float:
        """heading() -> float: deg

        Gets the heading angle relative to the starting orientation. It is a
        positive rotation around the :ref:`z-axis in the robot
        frame <robotframe>`, prior to applying any tilt rotation.

        For a vehicle viewed from the top, this means that
        a positive heading value corresponds to a counterclockwise rotation.

        .. note:: This method is not yet implemented.

        Returns:
            Heading angle relative to starting orientation.

        """

    def reset_heading(self, angle: Number) -> None:
        """reset_heading(angle)

        Resets the accumulated heading angle of the robot.

        .. note:: This method is not yet implemented.

        Arguments:
            angle (Number, deg): Value to which the heading should be reset.
        """

    @overload
    def angular_velocity(self, axis: Axis) -> float:
        ...

    @overload
    def angular_velocity(self) -> Matrix:
        ...

    def angular_velocity(self, *args):
        """
        angular_velocity(axis) -> float: deg/s
        angular_velocity() -> vector: deg/s

        Gets the angular velocity of the device along a given axis in
        the :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axis along which the angular velocity should be
                         measured.
        Returns:
            Angular velocity along the specified axis. If you specify no axis,
            this returns a vector of accelerations along all axes.
        """


class CommonColorSensor:
    """Generic color sensor that supports Pybricks color calibration."""

    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def color(self) -> Color:
        """color() -> Color

        Scans the color of a surface.

        You choose which colors are detected using the
        ``detectable_colors()`` method. By default, it detects
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, or ``Color.NONE``.

        Returns:
            Detected color.
        """

    def hsv(self) -> Color:
        """hsv() -> Color

        Scans the color of a surface.

        This method is similar to ``color()``, but it gives the full range
        of hue, saturation and brightness values, instead of rounding it to the
        nearest detectable color.

        Returns:
            Measured color. The color is described by a hue (0--359), a
            saturation (0--100), and a brightness value (0--100).
        """

    def ambient(self) -> int:
        """ambient() -> int: %

        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0% (dark)
            to 100% (bright).
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        Measures how much a surface reflects the light emitted by the
        sensor.

        Returns:
            Measured reflection, ranging from 0% (no reflection) to
            100% (high reflection).
        """

    @overload
    def detectable_colors(self, colors: Collection[Color]) -> None:
        ...

    @overload
    def detectable_colors(self) -> Collection[Color]:
        ...

    def detectable_colors(self, *args):
        """
        detectable_colors(colors)
        detectable_colors() -> Collection[Color]

        Configures which colors the ``color()`` method should detect.

        Specify only colors that you wish to detect in your application.
        This way, the full-color measurements are rounded to the nearest
        desired color, and other colors are ignored. This improves reliability.

        If you give no arguments, the currently chosen colors will be returned.

        Arguments:
            colors (list or tuple): List of :class:`Color <.parameters.Color>`
                objects: the colors that you want to detect. You can pick
                standard colors such as ``Color.MAGENTA``, or provide your
                own colors like ``Color(h=348, s=96, v=40)`` for even
                better results. You measure your own colors with the
                ``hsv()`` method.
        """


class AmbientColorSensor(CommonColorSensor):
    """Like CommonColorSensor, but also detects ambient colors when the sensor
    light is turned off"""

    def color(self, surface: bool = True) -> Optional[Color]:
        """color(surface=True) -> Color

        Scans the color of a surface or an external light source.

        You choose which colors are detected using the
        ``detectable_colors()`` method. By default, it detects
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, or ``Color.NONE``.

        Arguments:
            surface (bool): Choose ``true`` to scan the color of objects
                and surfaces. Choose ``false`` to scan the color of
                screens and other external light sources.

        Returns:
            Detected color.`
        """

    def hsv(self, surface: bool = True) -> Color:
        """hsv(surface=True) -> Color

        Scans the color of a surface or an external light source.

        This method is similar to ``color()``, but it gives the full range
        of hue, saturation and brightness values, instead of rounding it to the
        nearest detectable color.

        Arguments:
            surface (bool): Choose ``true`` to scan the color of objects
                and surfaces. Choose ``false`` to scan the color of
                screens and other external light sources.

        Returns:
            Measured color. The color is described by a hue (0--359), a
            saturation (0--100), and a brightness value (0--100).
        """
