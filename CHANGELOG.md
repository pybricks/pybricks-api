# Changelog

<!-- refer to https://keepachangelog.com/en/1.0.0/ for guidance -->

## Unreleased

## 3.2.0b1-r1 - 2022-06-09

## Added
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

## Changed
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
