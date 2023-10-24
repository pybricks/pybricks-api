from pybricks.tools import hub_menu

# This example assumes that you have three other programs in Pybricks Code,
# called "fly_mission", "drive_mission", and "zigzag". This example creates a
# menu that lets you pick which one to run.

# Choose a letter.
selected = hub_menu("F", "D", "Z")

# Based on the selection, run a program.
if selected == "F":
    import fly_mission
elif selected == "D":
    import drive_mission
elif selected == "Z":
    import zigzag
