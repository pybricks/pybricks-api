# Changelog

<!-- refer to https://keepachangelog.com/en/1.0.0/ for guidance -->

## Unreleased

## 3.5.0- 2024-04-11

### Changed
- Bump version to 3.5.0 without additional changes.

## 3.5.0b2 - 2024-04-05

### Added

- Added `pybricks.pupdevices.Remote.disconnect` method.
- Added blocks for `up`, `ready` and `stationary` for IMUs.
- Added `last` and `chr` parameters to `read_input_byte` and add blocks.
- Added block for the `in` operation.
- Add double ternary block.

## 3.5.0b1 - 2024-03-11

### Added

- Added `XboxController.rumble` method.
- Added block icons for `hub.system.set_stop_button` and `hub.system.shutdown`.
- Added program stop block (`raise SystemExit`).

## 3.4.1 - 2024-03-11

### Fixed

- Fixed Read The Docs virtual environment workflow.

## 3.4.0 - 2024-03-11

### Changed

- Update list block screenshots to match implementation.

## 3.4.0b5 - 2024-03-05

### Changed

- Updates for v3.4.0b3 firmware (out of sync with docs).
- Changed `hub.button` to `hub.buttons` on single button hubs. Access via
 `hub.button` will keep working in the firmware for backwards compatibility.

## 3.4.0b4 - 2024-02-14

### Added

- Added `pybricks.iodevices.XboxController` class.

### Changed

- Changed `buttons.pressed` return type to set.

## 3.4.0b3 - 2024-01-30

### Added

- Added `pybricks.robotics.Car` class.

### Changed

- Changed `pybricks.robotics.DriveBase` icon to two wheels instead of steering
  wheel, which will be used for the new car class.

## 3.4.0b2 - 2023-11-28

### Changed
- Include first batch of block coding images.

## 3.3.0 - 2023-11-24

### Changed
- Bump beta version to release version with no further changes.

## 3.3.0c1 - 2023-11-20

### Added
- Enabled tilt and orientation config for `MoveHub()`.
- Documented `Motor.close()`

## Fixed
- Fixed missing awaitable for `Remote.light` and LWP3 writes.

## 3.3.0b9 - 2023-10-26

### Changed
- Changed the beta feature for using the hub's gyro. Gyro control can now be
  toggled using `use_gyro` instead of using a separate `GyroDriveBase` class.
- Documentation updates to match firmware 3.3.0b5--3.3.0b9 updates.

### Added
- Added `set` to `ubuiltins` module.
- Basic multitasking docs.
- Awaitable keyword for awaitable methods and functions.

## 3.3.0b5 - 2023-05-16

### Added
- Documented new `hub.ble` methods.

## 3.3.0b4 - 2023-04-21

### Added
- Documented `integral_deadzone` in `Control.pid()`.
- Documented `Motor.model`. This can be used to view the estimated motor
  state and change its settings.
- Added `rotation`, `orientation`, `ready`, `stationary` and `settings` methods
  to `IMU` class.
- Added `GyroDriveBase` class to `pybricks.robotics`.

### Changed
- Change implementation status of `IMU.heading` and `IMU.reset_heading`. They
  are now implemented, with some limitations as noted in a note box.
- Moved `Matrix` and `vector` from `pybricks.geometry` to `pybricks.tools`.
- Moved `Axis` from `pybricks.geometry` to `pybricks.parameters`.

### Removed
- Removed `pybricks.geometry` module.

## 3.2.0 - 2022-12-20

### Changed
- Changed module TOC headings to make it easier to find things.

## 3.2.0c1 - 2022-12-09

### Changed
- Updated "front" side of the Technic Hub to be consistent with
  the Prime Hub.

## 3.2.0b6 - 2022-12-02

### Added
- Documented ``Stop.NONE`` and ``Stop.COAST_SMART``.
- Documented ``ujson`` module.
- Added `done` and `stalled` methods for `DriveBase`.

### Changed
- Changed `PrimeHub.display.image()` to `PrimeHub.display.icon()` and renamed
  its kwarg from `image` to `icon`.
- Improved presentation and docstrings of the ``ubuiltins`` and other
  MicroPython modules
- Moved the random numbers example for Move Hub to the Move Hub page.
- Moved `done()`, `stalled()`, `load()` from `Control` to `Motor` object.

## 3.2.0b5 - 2022-11-11

### Fixed
- Fixed Jedi code completion for `Color` and `Icon` classes in `pybricks.parameters`.

## 3.2.0b4 - 2022-10-21

### Added
- Code auto-completion for `EssentialHub`.
- Added `System.storage` method.

### Fixed
- Fixed some type hints in `parameters` submodule.

## 3.2.0b1-r3 - 2022-06-26

### Fixed
- Fixed more type hints and improved compatibility with jedi.

## 3.2.0b1-r2 - 2022-06-24

### Changed
- Moved remaining type hints from `.pyi` files to the python stub modules, and
  fixed numerous errors in the type hints throughout.

## 3.2.0b1-r1 - 2022-06-09

### Added
- Added `__init__.py` to `pybricks` package.

## 3.2.0b1 - 2022-06-02

### Added
- Code auto-completion for `hub.charger`, `hub.imu` and `hub.system`.
- Moved typing from several `.pyi` files to the actual python modules.

### Fixed
- Fixed code completion for `DCMotor` and `Motor` classes in MS Python VS Code extension.
- Fixed missing `DCMotor` type in `ev3devices`.
- Fixed type hint for `Motor.reset_angle()` in `pupdevices`.

### Changed
- Setter for acceleration can now also be used to set acceleration and
  deceleration to different values, using a two-valued tuple.

## 3.1.0 - 2021-12-16

### Added
- Added maximum voltage setter for `DCMotor` and `Motor`.
- Documented `DriveBase.curve()` method.

### Changed
- Removed `duty` setting from `Control.limits` method.
- Removed `integral_range` setting from `Control.pid` method.

### Fixed
- Fixed link to Color Light Matrix page.
- Fixed link to Inventor Hub page.

## 3.1.0rc1 - 2021-11-19

### Added
- Added `ColorLightMatrix` class.
- Added `LWP3Device` class.

**NOTE: version number after this point were from JavaScript package and do
not correspond to Pybricks firmware version numbers.**

## 1.6.0 - 2021-08-30

### Added
- MicroPython module documentation.
- Examples for hub system functions including stop button and shutdown.

### Changed
- Build IDE docs as main docs with minor changes, instead of a completely
  separate build.
- Moved motor control documentation to the motor page.

## 1.5.0 - 2021-07-01

### Added
- Documentation for Powered Up Remote Control.

## 1.4.0 - 2021-06-23

### Added
- Enabled beta content that was hidden for the 3.0 release.
- Added notice about using the latest beta version.

## 1.3.3 - 2021-05-21

### Changed
- Match example snippet styling to IDE.
- Add more examples.

## 1.3.2 - 2021-04-26

### Changed
- Theme style fixes.
- Example code fixes
- Match doc version to firmware version.

## 1.3.1 - 2021-04-12

### Changed
- Upgrade sphinx and rtd-theme to fix style issues.

## 1.3.0 - 2021-04-12

### Removed
- Removed features which not be in the official 3.0 release. These features
  are still in beta. They'll come back in future releases once tested.

## 1.2.0 - 2021-04-09

### Changed
- Moved installation guide to external site.

## 1.1.1 - 2021-02-14

### Added
- Added installation guide.
- Various documentation fixes.

## 1.1.0 - 2021-01-28

### Added
- Scrollbar styling.

## 1.0.0 - 2021-01-25

### Added
- Sphinx build output.
