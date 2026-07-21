from pybricks.tools import  run_task, hub_menu
#
# import the function that stops the robot's motion 
#
from robot_library import stopEverything()

#
# import the functions from each of the robots tasks that execute the task.
# NOTE: run_task() is not used in the three tasks since main function is called from menu
#
from robot_task1 import robot_task1_run
from robot_task2 import robot_task2_run
from robot_task3 import robot_task3_run

while True:
    selected = hub_menu("M","1","2","3","X")

    try:
        if selected == "M":
            # does nothing. used to show menu is active
            break
        if selected == "1":
            # wait for 1 second to get operator's fingers out of the way before robot moves
            wait(1000)
            # run robot task 1
            run_task(robot_task1_run())
        elif selected == "2":
            wait(1000)
            run_task(robot_task2_run())
        elif selected == "3":
            wait(1000)
            run_task(robot_task3_run())
        elif selected == "X":
            # runs that task the stops the robot's motion
            run_task(stopEverything())
            break

    except BaseException as menuException:
        print("Stop was Pressed or a Critical Error Occured. Stopping all motors.")
        print(menuException)
        run_task(stopEverything())
        break

print ("End of Menu - if you see this, there might be a problem.")
