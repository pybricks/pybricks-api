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
