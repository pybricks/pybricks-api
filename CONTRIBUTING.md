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

        prefix: subject

        body...

- Use a prefix to categorize the change. Usually this is the path the the file
  being changed. 
  - If it is a documentation change, it can be shortened to `doc/<file>` (omit
    `api` from the path).
  - If it is an API change (in the `pybricks` folder), write `api/<file>` 
    instead of `pybricks/<file>`.
- The subject briefly describes _what_ was changed, e.g. `fix typo`.
- The body describes _why_ the change was made, e.g. `The word "sensor" was
  spelled incorrectly`.
- See the [commit history][commits] for more examples.

[commits]: https://github.com/pybricks/pybricks-api/commits/master


**Development environment:**

Prerequisites:
- [VS Code][vscode] (optional but recommended)
- [Git][git]
- [Python 3][python]
- [Poetry][poetry]

Information on installing prerequisites can be found on the [pybricks-micropython
wiki][wiki].

Initial setup:

    git clone --recursive https://github.com/pybricks/pybricks-api
    cd pybricks-api
    poetry install

Build docs:

    # Linux
    poetry run make -C doc html
    xdg-open doc/api/build/html/index.html

    # macOS
    poetry run make -C doc html
    open doc/api/build/html/index.html

    # Windows (PowerShell)
    poetry run doc\make.bat html
    Invoke-Item doc\api\build\html\index.html

Linting:

    poetry run flake8  # check Python
    poetry run doc8  # check Restructured Text

[vscode]: https://code.visualstudio.com/
[git]: https://git-scm.com/
[python]: https://www.python.org/
[poetry]: https://python-poetry.org/
[wiki]: https://github.com/pybricks-micropython/wiki
