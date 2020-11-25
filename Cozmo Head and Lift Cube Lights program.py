# Head and Lift Movement Cozmo Codes: Python

import cozmo
import time

from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
def light(robot: cozmo.robot.Robot):
    
 cube1 = robot.world.get_light_cube(LightCube1Id)
 cube2 = robot.world.get_light_cube(LightCube2Id)
 cube3 = robot.world.get_light_cube(LightCube3Id)

 robot.move_lift(1)
 robot.move_head(1)
 cube1.set_lights(cozmo.lights.blue_light)
 time.sleep(1)
 
 robot.move_lift(-1)
 robot.move_head(-1)
 cube1.set_lights(cozmo.lights.green_light)
 time.sleep(1)
 
 robot.move_lift(1)
 robot.move_head(1)
 cube1.set_lights(cozmo.lights.blue_light) 
 time.sleep(1)
 
 robot.move_lift(-1)
 robot.move_head(-1)
 cube1.set_lights(cozmo.lights.green_light)
 time.sleep(1)

 robot.move_lift(1)
 robot.move_head(1)
 cube1.set_lights(cozmo.lights.blue_light) 
 time.sleep(1)

 robot.move_lift(-1)
 robot.move_head(-1)
 cube1.set_lights(cozmo.lights.green_light)
 time.sleep(1)

 #Cozmo 1 talks to Cozmo 2


cozmo.run_program(light)
