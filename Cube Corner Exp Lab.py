import cozmo
import time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
def light(robot: cozmo.robot.Robot):  
 cube1 = robot.world.get_light_cube(LightCube1Id)
 cube2 = robot.world.get_light_cube(LightCube2Id)
 cube3 = robot.world.get_light_cube(LightCube3Id)
 for i in range(10):
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    cube1.set_light_corners(cozmo.lights.green_light, cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.blue_light)
    cube2.set_light_corners(cozmo.lights.green_light, cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.blue_light)
    cube3.set_light_corners(cozmo.lights.green_light, cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.blue_light) 
    time.sleep(.1)
    robot.set_all_backpack_lights(cozmo.lights.green_light)
    cube1.set_light_corners(cozmo.lights.blue_light, cozmo.lights.green_light, cozmo.lights.blue_light, cozmo.lights.blue_light)
    cube2.set_light_corners(cozmo.lights.blue_light, cozmo.lights.green_light, cozmo.lights.blue_light, cozmo.lights.blue_light)
    cube3.set_light_corners(cozmo.lights.blue_light, cozmo.lights.green_light, cozmo.lights.blue_light, cozmo.lights.blue_light) 
    time.sleep(.1)
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    cube1.set_light_corners(cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.green_light, cozmo.lights.blue_light)
    cube2.set_light_corners(cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.green_light, cozmo.lights.blue_light)
    cube3.set_light_corners(cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.green_light, cozmo.lights.blue_light) 
    time.sleep(.1)
    robot.set_all_backpack_lights(cozmo.lights.green_light)
    cube1.set_light_corners(cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.green_light)
    cube2.set_light_corners(cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.green_light)
    cube3.set_light_corners(cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.green_light) 
    time.sleep(.1)
cozmo.run_program(light)
 
 
# cube1.set_lights(cozmo.lights.white_light)
#  cube1.set_light_corners(light1, light2, light3, light4)
#  cube1.set_light_corners(cozmo.lights.green_light, cozmo.lights.red_light, cozmo.lights.blue_light, cozmo.lights.off_light)

"""Cozmo Actions
# class cozmo.action.EvtActionCompleted(**kwargs)
# class cozmo.robot.Robot(conn, robot_id: int, is_primary: bool, **kw)
# turn_in_place(angle, in_parallel=False, num_retries=0, speed=None, accel=None, angle_tolerance=None, is_absolute=False)
# add_event_handler(event, f)
# in_parallel=True
"""
