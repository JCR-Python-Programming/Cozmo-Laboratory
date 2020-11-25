import cozmo
import time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
def light(robot: cozmo.robot.Robot):
    cube1 = robot.world.get_light_cube(LightCube1Id)
    cube2 = robot.world.get_light_cube(LightCube2Id)
    cube3 = robot.world.get_light_cube(LightCube3Id)
    robot.move_head(-1)
    robot.move_lift(-1)
    robot.set_all_backpack_lights(cozmo.lights.green_light)
    cube1.set_lights(cozmo.lights.green_light)
    cube2.set_lights(cozmo.lights.red_light)
    cube3.set_lights(cozmo.lights.red_light)
    for i in range(5):
        robot.say_text("Power Cube").wait_for_completed()
        robot.set_all_backpack_lights(cozmo.lights.red_light)
        cube1.set_lights(cozmo.lights.red_light)
        cube2.set_lights(cozmo.lights.green_light)
        cube3.set_lights(cozmo.lights.green_light)
        robot.move_head(1)
        robot.move_lift(1)        
        robot.say_text(str(i+1)).wait_for_completed()
        robot.set_all_backpack_lights(cozmo.lights.white_light)
        cube1.set_lights(cozmo.lights.white_light)
        cube2.set_lights(cozmo.lights.blue_light)
        cube3.set_lights(cozmo.lights.blue_light)
        robot.move_head(-1)
        robot.move_lift(-3)        
        time.sleep(2)
cozmo.run_program(light)

# robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

# robot.move_head(1) Moves robot head all the way up 45 degrees
# robot.move_head(-1) Moves robot head all the way down -45 degrees

# robot.move_lift(1) All the way up
# robot.move_lift(-1) all the way down
# set_light_corners(light1, light2, light3, light4)
