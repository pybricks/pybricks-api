#!/usr/bin/env python3
"""Generates hub-specific examples from common template script."""

import pathlib

# Make build directory.
dir_path = pathlib.Path(__file__).parent
build_path = dir_path / "build"
build_path.mkdir(exist_ok=True)

# Get list of scripts to be parsed.
file_paths = [f for f in dir_path.glob("*.py") if f.stem != "make_examples"]

# Go through all template scripts
for file_path in file_paths:

    with open(file_path) as template:

        # First line contains hub info
        hubs = template.readline().strip().split()[3:]

        print("Converting", template.name, "to", hubs)

        for hub in hubs:
            # Path to hub-specific output script.
            gen_path = build_path / (file_path.stem + "_" + hub.lower() + ".py")

            # Reset source script and skip over header.
            template.seek(0)
            template.readline()

            # Open destination script:
            with open(gen_path, "w") as dest_file:

                # Read script line by line.
                for line in template.readlines():

                    # Replace hub name if present.
                    dest_file.writelines(line.replace("ThisHub", hub))
