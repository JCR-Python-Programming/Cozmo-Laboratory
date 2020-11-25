
# This is a Phython Program Example:
# Copy this sample Light Cubes program into your IDLE Editor,
# Save this small cube light program as Light Cubes.py
# Run the Light Cubes program. Each cube stays lit for about 5 seconds

import cozmo
import time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
def light(robot: cozmo.robot.Robot):
 cube1 = robot.world.get_light_cube(LightCube1Id)
 cube2 = robot.world.get_light_cube(LightCube2Id)
 cube3 = robot.world.get_light_cube(LightCube3Id)
 cube1.set_lights(cozmo.lights.red_light)
 cube2.set_lights(cozmo.lights.green_light)
 cube3.set_lights(cozmo.lights.blue_light)
 time.sleep(5)
cozmo.run_program(light)

#  Once you try this simple cube program
#  Try the program below, but start a fresh Python project first.
#  Next, only copy the text, (not the quote marks)
# Quote marks are for extened comments about the program, once removed, the program is ready to copy into your IDLE Editor
#  Save the new Python program as Backpack Light.py

"""
import cozmo
import time
def light(robot: cozmo.robot.Robot):
    for _ in range(5):
     robot.set_all_backpack_lights(cozmo.lights.blue_light)
     time.sleep(.2)
     robot.set_all_backpack_lights(cozmo.lights.green_light)
     time.sleep(.2)
     robot.set_all_backpack_lights(cozmo.lights.red_light)
     time.sleep(.2)
     robot.set_all_backpack_lights(cozmo.lights.blue_light)
     time.sleep(.2)
     robot.set_all_backpack_lights(cozmo.lights.green_light)
     time.sleep(.2)
     robot.set_all_backpack_lights(cozmo.lights.red_light)
     time.sleep(.2)
cozmo.run_program(light)
def cozmo_program(robot: cozmo.robot.Robot):
 robot.say_text("Loop Experiment works").wait_for_completed()
 print("Cozmo Prints on screen Success")
cozmo.run_program(cozmo_program)
"""
