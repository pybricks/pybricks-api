#!/usr/bin/env python3

import email.parser
import json
import pathlib
import shutil
import subprocess
import sys
import zipfile

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <version>", file=sys.stderr)
    sys.exit(1)

VERSION = sys.argv[1]

ROOT_DIR = pathlib.Path(__file__).parent.resolve()
JEDI_SRC_DIR = (ROOT_DIR / ".." / ".." / "jedi").resolve()
BUILD_DIR = (ROOT_DIR / "build").resolve()

package_json = {
    "name": "@pybricks/jedi",
    "version": VERSION,
    "description": "Binary distribution of pybricks-jedi Python package and dependencies for use with Pyodide.",
    "repository": {
        "type": "git",
        "url": "https://github.com/pybricks/pybricks-api",
        "directory": "npm/jedi",
    },
    "publishConfig": {"registry": "https://registry.npmjs.org", "access": "public"},
}

license_identifiers: set[str] = set()
license_text: dict[str, str] = {}
whl_map: dict[str, str] = {}

# ensure empty build directory so we don't end up with stale files
shutil.rmtree(BUILD_DIR, True)
BUILD_DIR.mkdir()

# build pybricks-jedi wheel from local source
subprocess.check_call(["poetry", "build", "--format=wheel"], cwd=JEDI_SRC_DIR)

# copy locally built wheel to build dir
for whl in (JEDI_SRC_DIR / "dist").glob("pybricks_jedi-*.whl"):
    shutil.copy(whl, BUILD_DIR)

# download transitive dependencies from PyPI, using the local wheel to satisfy pybricks-jedi itself
subprocess.check_call(
    [
        sys.executable,
        "-m",
        "pip",
        "download",
        "--only-binary=any",
        f"--find-links={BUILD_DIR}",
        "pybricks-jedi",
    ],
    cwd=BUILD_DIR,
)

# extract info from wheel files to generate javascript package files
for whl in BUILD_DIR.glob("*.whl"):
    with zipfile.ZipFile(whl) as f:

        def is_dist_info_metadata(info: zipfile.ZipInfo):
            return info.filename.endswith(".dist-info/METADATA")

        def is_dist_info_license(info: zipfile.ZipInfo):
            return ".dist-info" in info.filename and "LICENSE" in info.filename

        metadata = next(filter(is_dist_info_metadata, f.filelist))

        with f.open(metadata.filename) as mf:
            meta = email.parser.BytesParser().parse(mf)

            # extract package name from metadata
            name = meta["Name"]

            if not name:
                raise RuntimeError(f"missing 'Name' in {whl.name} METADATA")

            whl_map[name] = whl.name

            # extract license identifier from metadata

            license = meta["License"]

            if not license:
                # some packages are missing license in metadata
                if whl.name.startswith("typing_extensions-"):
                    license = "Python-2.0"
                else:
                    raise RuntimeError(f"missing 'License' in {whl.name} METADATA")

            license_identifiers.add(license)

        if whl.name.startswith("pybricks_jedi-"):
            with open(JEDI_SRC_DIR / "LICENSE") as lf:
                license_text[whl.name] = lf.read()
        else:
            try:
                license = next(filter(is_dist_info_license, f.filelist))
            except StopIteration:
                raise RuntimeError(f"missing license for {whl.name}")

            with f.open(license) as lf:
                license_text[whl.name] = lf.read().decode()


# generate package.json file

# create "license" item from collected license identifiers
package_json["license"] = (
    license_identifiers[0]
    if len(license_identifiers) < 2
    else f"({' AND '.join(license_identifiers)})"
)

# create "exports" item from collect whl map
package_json["exports"] = {f"./{k}.whl": f"./{v}" for k, v in whl_map.items()}

with open(BUILD_DIR / "package.json", "w") as f:
    json.dump(package_json, f, indent=2)

# generate LICENSE file

NEWLINE = "\n"
DIVIDER = "=" * 80 + NEWLINE
with open(BUILD_DIR / "LICENSE", "w") as f:
    for whl, text in license_text.items():
        f.write(DIVIDER)
        f.write(whl)
        f.writelines([NEWLINE, DIVIDER, NEWLINE])
        f.write(text)
        f.write(NEWLINE)

# copy additional files

for file in ("README.md",):
    shutil.copy(ROOT_DIR / file, BUILD_DIR / file)
