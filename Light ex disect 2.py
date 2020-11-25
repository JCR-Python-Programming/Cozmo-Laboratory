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
