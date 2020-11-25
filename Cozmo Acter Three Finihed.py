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
 cube3.set_lights(cozmo.lights.green_light)
 robot.drive_straight(distance_mm(270), speed_mmps(40)).wait_for_completed()

 robot.move_lift(1)
 cube3.set_lights(cozmo.lights.red_light) 
 robot.drive_straight(distance_mm(25), speed_mmps(20)).wait_for_completed()

 robot.move_lift(-1)
 robot.move_head(-1)
 cube3.set_lights(cozmo.lights.blue_light)
 time.sleep(1)
 
 robot.move_lift(1)
 robot.move_head(1)
 cube3.set_lights(cozmo.lights.green_light)
 time.sleep(1)

 robot.move_lift(-1)
 robot.move_head(-1)
 cube3.set_lights(cozmo.lights.blue_light) 
 time.sleep(1)

 robot.move_lift(1)
 robot.move_head(1)
 cube3.set_lights(cozmo.lights.green_light)
 time.sleep(1)

 robot.move_lift(-1)
 robot.move_head(-1)
 cube3.set_lights(cozmo.lights.blue_light)
 robot.say_text("Yucky, this part of the video is so boring!").wait_for_completed()
 robot.say_text("But Cozmo! This is the best part of this video, our viewers can learn something educational, and have lots of fun at the same time.").wait_for_completed()
 robot.say_text("I just want to go outside and play in the snow all day long!").wait_for_completed()
 robot.say_text("Cozmo! we are robots, made out of plastic, and sometimes plastic can break in cold weather, You should know that!").wait_for_completed()
 robot.say_text("Well, let's go for a swim in the pool instead then!").wait_for_completed()
 robot.say_text("Cozmo! We cannot do that either, robots and water do not mix too well together! We will short out if we go in the water.").wait_for_completed()
 robot.say_text("Are we waterproof Robots?").wait_for_completed()
 robot.say_text("No Cozmo, We are not waterproof robots, and we cannot swim at all. But, we are kid approved for kids and adults of all ages, and every kid loves Cozmo, the Robot!").wait_for_completed()
 robot.say_text("Cozmo, I have an idea, Let's go sky diving, without a parachute, we don't need snow or water to do that, do we?").wait_for_completed()
 robot.say_text("Cozmo! Are you crazy? We will smash to bits, after we wack the ground at about a million miles an hour!").wait_for_completed()
 robot.say_text("Hmm, What can we do then Cozmo?").wait_for_completed()
 robot.say_text("Cozmo, I have an idea, We finish this video, like the good little robots that we are, We don't need snow, we don't need water, and we sure don't need a parachute to do that.").wait_for_completed()
 robot.say_text("all we need to do, is finish this special effects video lesson, I'm not too impressed, having to do this video either, But our master makes us do it anyway. Yucky yucky Yucky!").wait_for_completed()
 time.sleep(10)
cozmo.run_program(light)
