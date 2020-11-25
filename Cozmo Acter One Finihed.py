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

 robot.move_lift(1)
 cube1.set_lights(cozmo.lights.red_light) 
 robot.drive_straight(distance_mm(25), speed_mmps(20)).wait_for_completed()

 robot.move_lift(-1)
 robot.move_head(-1)
 cube1.set_lights(cozmo.lights.blue_light)
 time.sleep(1)
 
 robot.move_lift(1)
 robot.move_head(1)
 cube1.set_lights(cozmo.lights.green_light)
 time.sleep(1)

 robot.move_lift(-1)
 robot.move_head(-1)
 cube1.set_lights(cozmo.lights.blue_light) 
 time.sleep(1)

 robot.move_lift(1)
 robot.move_head(1)
 cube1.set_lights(cozmo.lights.green_light)
 time.sleep(1)

 robot.move_lift(-1)
 robot.move_head(-1)
 cube1.set_lights(cozmo.lights.blue_light)
 
 robot.say_text("Hello world! I am the one and only, yup! the one in the middle! That's me! Cozmo's younger brother Cozmo, liquid metal collector's edition!").wait_for_completed()
 robot.say_text("Yet, you can see two other cozmos in this Sony Vegas special effects Video example! Do you wonder how it's done?").wait_for_completed()
 robot.say_text("Let me show you how to create a special effects video, just like this Sony Vegas special effects video example.").wait_for_completed()
 robot.say_text("As you can see, there are three pre,rendered video layers of myself in a different posed position, Each layer is a separate pre,rendered video of myself.").wait_for_completed()
 robot.say_text("Each layer, is also cropped in all three of my pre-rendered video posed positions. Each video layer is equal timing in frames as well.").wait_for_completed()
 robot.say_text("Once all three videos are rendered together, when played back, I look like there are more than one Cozmo,Yet, I am the real deal, who sits in between two other fake Cozmos.").wait_for_completed()
 robot.say_text("Most important, the lighting has to be well lit, and even Steven, so that all three video layers of myself, become seamless, over layered videos.").wait_for_completed()
 robot.say_text("One more, very important lesson to remember, never, ever move your video camera, or webcam, while creating a special effects video like this one.").wait_for_completed()
 robot.say_text("If you move your video camera, or webcam, you will ruin this video's special effect.").wait_for_completed()
 robot.say_text("In fact, if you move your video camera, or webcam at all, even a little bit. You will have to re-create the whole video all over again! and believe me, you do not want to do that!").wait_for_completed()
 robot.say_text("Also, make sure your camera, or webcam is positioned properly to be able to capture your subjects in camera range, with lots of space in between the subjects, so they won't overlap.").wait_for_completed()
 robot.say_text("If your pre rendered video subjects are too close to one another, they will overlap in the final video rendering. Be careful, to keep enough space in between your subjects at all times.").wait_for_completed()
 robot.say_text("and, most importantly. Ponder into Wonder! Be creative! and Have lots of fun learning how to create special effects videos with Cozmo's younger brother, Cozmo!").wait_for_completed()
 cube1.set_lights(cozmo.lights.blue_light)
 robot.say_text("Next, I will show you how I can look like a ghost, and disappear like one too.").wait_for_completed()
 cube1.set_lights(cozmo.lights.red_light)
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 cube1.set_lights(cozmo.lights.blue_light)
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 cube1.set_lights(cozmo.lights.red_light)
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 cube1.set_lights(cozmo.lights.green_light)
 time.sleep(10)
cozmo.run_program(light)
