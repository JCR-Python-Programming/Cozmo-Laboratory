import time
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
def cozmo_program(robot: cozmo.robot.Robot):
    for i in range(10):
     cube1 = robot.world.get_light_cube(LightCube1Id)
     cube2 = robot.world.get_light_cube(LightCube2Id)
     cube3 = robot.world.get_light_cube(LightCube3Id)     
     robot.set_all_backpack_lights(cozmo.lights.blue_light)
     cube1.set_lights(cozmo.lights.blue_light)
     time.sleep(.2)     
     cube1.set_lights(cozmo.lights.off_light)
     robot.set_all_backpack_lights(cozmo.lights.red_light)
     cube2.set_lights(cozmo.lights.red_light)
     time.sleep(.2)
     cube2.set_lights(cozmo.lights.off_light)
     robot.set_all_backpack_lights(cozmo.lights.green_light)
     cube3.set_lights(cozmo.lights.green_light)
     time.sleep(.2)
     robot.set_all_backpack_lights(cozmo.lights.off_light)
     cube3.set_lights(cozmo.lights.off_light)
cozmo.run_program(cozmo_program)
