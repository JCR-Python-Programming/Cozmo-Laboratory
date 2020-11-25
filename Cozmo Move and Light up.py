import cozmo
import time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import degrees, distance_mm, speed_mmps
def light(robot: cozmo.robot.Robot):
 cube1 = robot.world.get_light_cube(LightCube1Id)
 cube2 = robot.world.get_light_cube(LightCube2Id)
 cube3 = robot.world.get_light_cube(LightCube3Id)
 robot.play_anim_trigger(cozmo.anim.Triggers.ReactToPokeStartled).wait_for_completed()
 robot.play_anim_trigger(cozmo.anim.Triggers.ReactToPokeStartled).wait_for_completed()
 robot.play_anim_trigger(cozmo.anim.Triggers.ReactToPokeStartled).wait_for_completed()
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail).wait_for_completed()
 robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail).wait_for_completed()
 robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail).wait_for_completed()
 robot.move_head(-1)
 cube1.set_lights(cozmo.lights.red_light)
 robot.drive_straight(distance_mm(200), speed_mmps(1000)).wait_for_completed()
 robot.turn_in_place(degrees(180)).wait_for_completed()
cozmo.run_program(light)
