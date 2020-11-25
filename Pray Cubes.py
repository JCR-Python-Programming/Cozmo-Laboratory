import time
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
def cozmo_program(robot: cozmo.robot.Robot):
  cube1 = robot.world.get_light_cube(LightCube1Id)
  cube2 = robot.world.get_light_cube(LightCube2Id)
  cube3 = robot.world.get_light_cube(LightCube3Id)
  for i in range(3):
   cube1.set_lights(cozmo.lights.blue_light)
   time.sleep(1)
   cube2.set_lights(cozmo.lights.green_light)
   time.sleep(1)
   cube3.set_lights(cozmo.lights.red_light)
   time.sleep(1)
cozmo.run_program(cozmo_program)
