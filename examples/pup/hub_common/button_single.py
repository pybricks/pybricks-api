# ThisHub = MoveHub CityHub TechnicHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color, Button
from pybricks.tools import wait, StopWatch

# Initialize the hub.
hub = ThisHub()

sys_tick = StopWatch()  # free running

# Disable the stop button.
hub.system.set_stop_button(None)
hub_button_start = 0  # sys_tick time the press started.


def check_button_2s_4s():
    # returns False if button is not pressed
    # returns True if button is pressed quickly (<1.5s)
    # stops script if button is pressed for 2s (and released)
    # Turns off Hub if button is pressed for 4s
    global hub_button_start

    if hub.button.pressed():
        if hub_button_start == 0:        # start press time
            hub_button_start = sys_tick.time()
        elif (sys_tick.time() - hub_button_start) >= 4000:
            hub.system.shutdown()        # power off
    else:                                # button release or no press
        if hub_button_start > 0:         # a running press
            if (sys_tick.time() - hub_button_start) < 1500: # quick action
                hub_button_start = 0     # stop press time
                return True
            elif (sys_tick.time() - hub_button_start) < 4000:
                raise SystemExit         # Stop script
    return False


while sys_tick.time() < 60000:  # or: while True
    wait(100)
    if check_button_2s_4s():
        hub.light.on(Color.GREEN)
        wait(500)
    else:
        hub.light.on(Color.RED)
		
# Enable the stop button again.
hub.system.set_stop_button(Button.CENTER)
