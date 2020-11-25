import cozmo
import time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import degrees, distance_mm, speed_mmps
def light(robot: cozmo.robot.Robot):
 cube1 = robot.world.get_light_cube(LightCube1Id)
 cube2 = robot.world.get_light_cube(LightCube2Id)
 cube3 = robot.world.get_light_cube(LightCube3Id)
 robot.move_head(1)
 robot.move_lift(-1) 
 cube1.set_lights(cozmo.lights.green_light)
 robot.drive_straight(distance_mm(270), speed_mmps(40)).wait_for_completed()
 cube1.set_lights(cozmo.lights.red_light)
 robot.move_lift(1)
 robot.drive_straight(distance_mm(25), speed_mmps(20)).wait_for_completed()
 robot.move_lift(-1)
 cube1.set_lights(cozmo.lights.blue_light)
 time.sleep(10)  
cozmo.run_program(light)

#robot.turn_in_place(degrees(30)).wait_for_completed()
