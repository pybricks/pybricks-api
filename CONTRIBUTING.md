**Project:** `pybricks-api`

**Acceptable changes:**

- Fixing typos, spelling, grammar, etc.
- Clarifying existing documentation.
- Improving code completion/intellisense.

Other more substantial changes should be discussed first by [opening an issue
on GitHub][issues]. Proposals for new APIs should be discussed in the
[pybricks-micropython][pbmp] repository since that is where the new features
will actually be implemented.


[issues]: https://github.com/pybricks/pybricks-api/issues
[pbmp]: https://github.com/pybricks/pybricks-micropython


**Commit messages:**

- Commit messages have a one-line subject, a blank line and a multiline body:

        prefix: Subject of the change.

        body...

- Use a prefix to categorize the change:
  - Use the import path as the prefix whenever possible. Examples:
     - pybricks.tools: Add StopWatch class.
     - pybricks.tools: Reorganize RST files.
     - pybricks.tools.StopWatch: Fix return type.
     - pybricks.tools.wait: Add example of waiting.
     - pybricks.pupdevices: Fix all sensor class ports.
     - umath.sin: Fix spelling of Hypotenuse.
  - If an import path makes no sense, just use the file path without
    extensions:
     - .vscode/settings: Fix file associations.
- The subject briefly describes _what_ was changed. Use a short full sentence
  as in the examples above.
- The body describes _why_ the change was made, e.g. `The word "sensor" was
  spelled incorrectly`.

[commits]: https://github.com/pybricks/pybricks-api/commits/master

**General docstring principles:**

The stubs libraries in this repository have two different purposes:
1. Auto-generating documentation with Sphinx. For this purpose, the
   documentation should be concise and clear.
2. Provide autocomplete and intellisense in code editors. For this purpose,
   the code needs to be 100% correct. This way, computers can parse your code
   correctly and tell you when something is wrong.

Since these objectives don't always align, we address these separately in the
stubs library:

1. The first line(s) of the docstring contain the function or method signature
   as it should be displayed in the human-readable documentation.
2. The real function signature can be as complex as it needs to be to make it
   correct for intellisense. Overloads can be uses if needed.

In the rare case where the docstring signature is the same as the typed
version, we'll still include it for consistency.

**Docstring details:**

Make sure to look at existing function signatures and docstrings for
inspiration when documenting new functionality. As an example, consider:

```python
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
```
The real method signature at the top contains the full detail, including the
type of each argument and return value.

The docstring starts with the signature. Use more than one signature if needed
to represent overloaded methods. The signatures are written in the way they
should be displayed in the docs:
- Argument types are omitted because they are also shown with the argument
  description below.
- Default values should be given (``then=Stop.COAST``).
- The return type should be given (``-> int``). When applicable, include
  the unit of the return value, so it becomes ``-> int: deg``

Then follows a concise description of what this method, function, or class
does.

Then follows a list of arguments:
- For each argument, include the expected type and unit if applicable, e.g.
  ``(int)`` or ``(Number, deg/s)``.
- Use ``Number`` when ``int`` and ``float`` are both allowed.
- If the description is long, use the indentation shown above.
- Make it readable. Instead
  of ``Union[float, SupportsFloat, complex, SupportsComplex]``,
  just say _float or complex_.

Then follows a description of the return value. The type is omitted here since
it is already include in the docstring signature.

**Development environment:**

Prerequisites:
- [VS Code][vscode] (optional but recommended)
- [Git][git]
- [Python 3][python]
- [Poetry][poetry]

Information on installing prerequisites can be found on the
[pybricks-micropython contributor's guide][contributing].

Initial setup:

    git clone --recursive https://github.com/pybricks/pybricks-api
    cd pybricks-api
    poetry install

Build docs:

    # Linux
    poetry run make -C doc html
    xdg-open doc/main/build/html/index.html

    # macOS
    poetry run make -C doc html
    open doc/main/build/html/index.html

    # Windows (PowerShell)
    poetry run doc\make.bat html
    Invoke-Item doc\main\build\html\index.html

Building IDE docs variant:

    # Linux/macOS
    poetry run make -C doc html TAG=ide

    # Windows (PowerShell)
    $env:TAG="ide"
    poetry run doc\make.bat html

Linting:

    poetry run flake8  # check Python
    poetry run doc8  # check Restructured Text

[vscode]: https://code.visualstudio.com/
[git]: https://git-scm.com/
[python]: https://www.python.org/
[poetry]: https://python-poetry.org/
[contributing]: https://github.com/pybricks/pybricks-micropython/blob/master/CONTRIBUTING.md
