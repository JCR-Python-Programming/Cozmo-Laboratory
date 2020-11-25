import cozmo
import time
def light(robot: cozmo.robot.Robot):
    for _ in range(2):
     robot.set_all_backpack_lights(cozmo.lights.blue_light)
     robot.say_text("Blue Light").wait_for_completed()
     robot.set_all_backpack_lights(cozmo.lights.green_light)
     robot.say_text("Green Light").wait_for_completed()
     robot.set_all_backpack_lights(cozmo.lights.red_light)
     robot.say_text("Red Light").wait_for_completed()
     robot.set_all_backpack_lights(cozmo.lights.blue_light)
     robot.say_text("Blue Light").wait_for_completed()
     robot.set_all_backpack_lights(cozmo.lights.red_light)
     robot.say_text("all systems checked").wait_for_completed()
cozmo.run_program(light)
def cozmo_program(robot: cozmo.robot.Robot):
 robot.say_text("Loop is finished, exicution is complete").wait_for_completed()
cozmo.run_program(cozmo_program)
