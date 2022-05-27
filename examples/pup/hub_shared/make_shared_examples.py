#!/usr/bin/env python3
"""Replaces all instances of ExampleHub in template with actual hub names."""
import os

# Get list of scripts to be parsed
script_names = [f for f in os.listdir(".") if f != "make_shared_examples.py"]

# Go through all template scripts
for script in (open(f, "r") for f in script_names):

    # First line contains hub info
    hubs = script.readline().strip().split()[3:]

    print("Converting", script.name, "for", hubs)

    for hub in hubs:
        # Determine path to the hub
        hub_path = os.path.join("..", "hub_" + hub.lower())

        # Reset source script
        script.seek(0)
        script.readline()

        # Open destination script:
        with open(os.path.join(hub_path, script.name), "w") as dest_file:

            # Read script line by line
            for line in script.readlines():

                # Replace hub name if present
                dest_file.writelines(line.replace("ExampleHub", hub))
