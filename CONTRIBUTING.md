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

**Translating Code Examples:**

The documentation system supports translating comments in code examples without duplicating the code itself. This is particularly useful for maintaining example code in multiple languages while keeping the actual code synchronized.

Directory Structure:
```
examples/
├── micropython/
│   └── example.py          # Original example with English comments
└── translations/
    └── de/                 # Language code (e.g., 'de' for German)
        └── micropython/
            └── example.py.comments  # Translations file
```

Translation Files:
- Create a `.comments` file in the corresponding language directory
- Use the format: `original comment = translated comment`
- Each translation should be on a new line
- Lines starting with `#` are ignored (can be used for translator notes)

Example translation file (`example.py.comments`):
```
# Translations for example.py
Initialize the motor. = Initialisiere den Motor.
Start moving at 500 deg/s. = Beginne die Bewegung mit 500 Grad/Sekunde.
```

In RST files, use the `translated-literalinclude` directive instead of `literalinclude` to include code examples that should have translated comments:

```rst
.. translated-literalinclude::
    ../../../examples/micropython/example.py
```

The translation system will:
1. Include the original code file
2. If building for a non-English language, look for corresponding `.comments` file
3. Replace comments with translations if they exist
4. Fall back to original comments if no translation exists

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

Translations:

The documentation supports multiple languages through Sphinx's internationalization (i18n) feature.

Directory structure:
- `doc/locales/pot/` - Contains template (.pot) files generated by `make gettext`. These files contain all original strings that need to be translated.
- `doc/locales/<language>/LC_MESSAGES/` - Contains translation (.po) files for each language. These files must be directly in the LC_MESSAGES directory (not in subdirectories) and contain the actual translations that will be used to build the documentation.

Note about translations:
The translation system uses unique IDs (UUIDs) for each translatable string. This ensures that translations are preserved even if you move text to different files or lines. The source file locations are included as comments in the .po files to help track where translations are used.

Translation files:
- `.po` files are human-readable text files containing the translations. These should be committed to the repository.
- `.mo` files are compiled binary versions of .po files, generated automatically during build. These should not be committed.

To work with translations:

1. Generate translation templates:

       poetry run make -C doc gettext

   This creates .pot template files in `doc/locales/pot/`

2. Initialize or update a language (e.g., German 'de'):

       poetry run make -C doc update-po-de

   This creates or updates .po files in `doc/locales/de/LC_MESSAGES/`

3. Edit the .po files in `doc/locales/<language>/LC_MESSAGES/` to add translations

4. Build documentation for a specific language:

       poetry run make -C doc html-de    # For German
       poetry run make -C doc html-fr    # For French
       poetry run make -C doc html-ja    # For Japanese

When adding translations to the repository:
- Commit the .po files in `doc/locales/<language>/LC_MESSAGES/`
- Do not commit the .pot files in `doc/locales/pot/` (these are generated files)

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
