#!/usr/bin/env python3

from glob import glob
import json
import pathlib
import shutil

BUILD_DIR = (pathlib.Path(__file__).parent / "build").resolve()
IMAGE_DIR = (
    pathlib.Path(__file__).parent.parent.parent / "doc" / "main" / "diagrams"
).resolve()
HUBS = ["move", "city", "technic", "prime", "essential", "inventor"]

package_json = {
    "name": "@pybricks/images",
    "version": "1.3.0",
    "description": "Distribution of Pybricks images.",
    "license": "MIT",
    "repository": {
        "type": "git",
        "url": "https://github.com/pybricks/pybricks-api",
        "directory": "npm/images",
    },
    "publishConfig": {"registry": "https://registry.npmjs.org", "access": "public"},
    "exports": {},  # dynamically filled below
}

# ensure empty build directory so we don't end up with stale files
shutil.rmtree(BUILD_DIR, True)
BUILD_DIR.mkdir()

# copy the hub images
for h in HUBS:
    shutil.copyfile(IMAGE_DIR / f"icon_{h}hub.png", BUILD_DIR / f"hub-{h}.png")
    package_json["exports"][f"./hub-{h}.png"] = f"./hub-{h}.png"

# copy DFU Windows driver images
for path in glob("dfu_windows_*", root_dir=IMAGE_DIR):
    file = pathlib.Path(path).name
    shutil.copyfile(IMAGE_DIR / path, BUILD_DIR / file)
    package_json["exports"][f"./{file}"] = f"./{file}"

# generate package.json file

with open(BUILD_DIR / "package.json", "w") as f:
    json.dump(package_json, f, indent=2)

# copy additional files

ROOT_DIR = (pathlib.Path(__file__).parent).resolve()

for file in "README.md", "CHANGELOG.md", "LICENSE":
    shutil.copy(ROOT_DIR / file, BUILD_DIR / file)
