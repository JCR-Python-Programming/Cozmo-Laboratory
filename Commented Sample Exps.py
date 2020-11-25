# Robot.Play Animation Behavior
"""
anim = robot.play_anim_trigger(cozmo.anim.Triggers.AskToBeRightedRight)
anim.wait_for_completed()
anim = robot.play_anim_trigger(cozmo.anim.Triggers.AudioTestAnim)
anim.wait_for_completed()"""

"""import time
import cozmo
def cozmo_program(robot: cozmo.robot.Robot):   
 
cozmo.run_program(cozmo_program)"""

# anim Robot Play Trigger Behavior

"""import cozmo
def cozmo_program(robot: cozmo.robot.Robot):   
 anim = robot.play_anim_trigger(cozmo.anim.Triggers.GuardDogFakeout)
 anim.wait_for_completed()
cozmo.run_program(cozmo_program)"""

"""import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.say_text("and, most importantly. Ponder into Wonder! Be creative! and Have lots of fun learning how to create special effects videos with Cozmo's younger brother, Cozmo!").wait_for_completed()
cozmo.run_program(cozmo_program)"""

# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BlockReact)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.AudioTestAnim)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerGetOut)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerGetIn)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerIdeaToPlay)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerIntoScore1)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerIntoScore2)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerIntoScore3)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerRequestToPlay)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerTimeout)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BouncerWait)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidFirstBlockOnSide)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidFirstBlockUpright)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidLookForFace)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidReactToBase)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidSecondBlockOnSide)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidSecondBlockUpright)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidSuccess)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.BuildPyramidThankUser)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.AudioTestAnim)
# anim = robot.play_anim_trigger(cozmo.anim.Triggers.AskToBeRightedRight)
# anim.wait_for_completed()

# Robot Start Behavior

"""import time
import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.start_behavior(cozmo.behavior.BehaviorTypes.RollBlock).wait_for_completed() 
 robot.start_behavior(cozmo.behavior.BehaviorTypes.StackBlocks).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
cozmo.run_program(cozmo_program)"""

"""import cozmo
def cozmo_program(robot: cozmo.robot.Robot):   
 robot.say_text("Test Emotion", play_excited_animation=False).wait_for_completed()
cozmo.run_program(cozmo_program)"""

#  Example Drive and Turn #1

"""import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
 robot.drive_straight(distance_mm(200), speed_mmps(30)).wait_for_completed()
 robot.turn_in_place(degrees(90),speed=degrees(30)).wait_for_completed()
cozmo.run_program(cozmo_program)"""

# robot.drive_straight(distance_mm(150), speed_mmps(30)).wait_for_completed()
# robot.turn_in_place(degrees(90)).wait_for_completed()

# robot.drive_straight(distance_mm(200), speed_mmps(50)).wait_for_completed()
# robot.turn_in_place(degrees(90),speed=degrees(50)).wait_for_completed()
# robot.turn_in_place(degrees(90)).wait_for_completed()

# AcknowledgeFaceNamed
# AcknowledgeFaceUnnamed

"""Robot Behavior Triggers"""
# AcknowledgeFaceNamed
# AcknowledgeFaceUnnamed
# AudioTestAnim

""" robot.play_anim_trigger examples:"""
# robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail)

"""Head and Lift Movement"""
# robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
#  robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()
# class cozmo.robot.SetHeadAngle(angle, max_speed, accel, duration, warn_on_clamp, **kw)
# accel = None, duration = None, max_speed = None
# robot.move_head(-1), robot.move_lift(-1)
# class cozmo.robot.SetLiftHeight(height, max_speed, accel, duration, **kw)
# accel = None, duration = None, max_speed = None

# cozmo.objects.LightCubeIDs = [1, 2, 3]

"""Example Behavior #1

import cozmo
def cozmo_program(robot: cozmo.robot.Robot):   
robot.play_anim_trigger(cozmo.anim.Triggers.AcknowledgeFaceUnnamed).wait_for_completed()
cozmo.run_program(cozmo_program)

import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.set_head_light(True)
 robot.say_text("yeah, I did it!", play_excited_animation=True).wait_for_completed()
cozmo.run_program(cozmo_program)

Example Behavior #2

import cozmo
def cozmo_program(robot: cozmo.robot.Robot):   
 
cozmo.run_program(cozmo_program)"""

# Cube and Backpack Light Color Loop

"""import time
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
def cozmo_program(robot: cozmo.robot.Robot):
    for i in range(1000):
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
cozmo.run_program(cozmo_program)"""

"""import cozmo
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
cozmo.run_program(cozmo_program)"""

# cube1.set_light_corners(cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.off_light)

""" import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
   for _ in range(3):
    robot.set_all_backpack_lights(cozmo.lights.red_light)
    robot.drive_straight(distance_mm(300), speed_mmps(10)).wait_for_completed()
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.set_all_backpack_lights(cozmo.lights.red_light)
    robot.drive_straight(distance_mm(110), speed_mmps(10)).wait_for_completed()
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.set_all_backpack_lights(cozmo.lights.red_light)
    robot.drive_straight(distance_mm(300), speed_mmps(10)).wait_for_completed()
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.set_all_backpack_lights(cozmo.lights.red_light)
    robot.drive_straight(distance_mm(110), speed_mmps(10)).wait_for_completed()
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    robot.turn_in_place(degrees(90)).wait_for_completed()
cozmo.run_program(cozmo_program)
import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
   robot.say_text("Error! Error! Exterminait! Exterminait! Exterminait! Error! Error!").wait_for_completed()
cozmo.run_program(cozmo_program)

robot.turn_in_place(degrees(-90)).wait_for_completed()
robot.drive_straight(distance_mm(150), speed_mmps(10)).wait_for_completed()"""

"""import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
 robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
 robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()
cozmo.run_program(cozmo_program)"""

"""import cozmo
import time
def cozmo_program(robot: cozmo.robot.Robot): robot.move_head(-1)
 robot.move_lift(-1)
 robot.drive_wheels(50, 25)
 time.sleep(3)
 robot.move_head(1)
 robot.move_lift(1)
 robot.drive_wheels(50, -50)
 time.sleep(3)
cozmo.run_program(cozmo_program)"""

"""set_lift_height takes in a “height (float) – desired height for Cozmo’s lift 0.0 (bottom) to 1.0 (top) (we clamp it to this range internally).” - so because it’s already in 0 to 1 space you don’t generally need additional constants:
http://cozmosdk.anki.com/docs/generated/cozmo.robot.html#cozmo.robot.Robot.set_lift_height2
There is also a LiftPosition class which lets you convert between lift position as a distance (in millimeters) above the ground, the 0 to 1 ratio, and the angle in degrees of the lift arm (as technically the lift arm rotates when lifting up / down.):
http://cozmosdk.anki.com/docs/generated/cozmo.robot.html#cozmo.robot.LiftPosition
You can also see the ranges for the non-ratio lift values here:
http://cozmosdk.anki.com/docs/generated/cozmo.robot.html#cozmo.robot.MIN_LIFT_HEIGHT
So, the simplest equivalent for the example in your question is:
robot.set_lift_height(1.0).wait_for_completed()
robot.set_lift_height(0.0).wait_for_completed()
and to e.g. set it halfway up you’d just do:
robot.set_lift_height(0.5).wait_for_completed()"""

"""You can call wait_for_completed later (after you’ve started the actions running in parallel)
E.g:
robot.set_lift_height(1.0).wait_for_completed()
Is the same as writing:
# don't wait yet, just start the action and keep a reference to it
my_lift_action = robot.set_lift_height(1.0)
# ... do any other work you want to do...
# now wait on the action
my_lift_action.wait_for_completed()
So you can do e.g:
# don't wait yet, just start the action and keep a reference to it
my_lift_action = robot.set_lift_height(1.0)
my_head_action = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
# Now that they're both running together in parallel, wait for both of them
my_lift_action.wait_for_completed()
my_head_action.wait_for_completed()
There’s also a helper method wait_for_all_actions_completed:
http://cozmosdk.anki.com/docs/generated/cozmo.robot.html#cozmo.robot.Robot.wait_for_all_actions_completed1
so you can simplify the above to just this if you want:
robot.set_lift_height(1.0)
robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
# Now that they're both running together in parallel, wait for everything
robot.wait_for_all_actions_completed()"""

"""Can I make cozmo see and pick only the cube, I want, with Actions?
Yes - see the documentation here: http://cozmosdk.anki.com/docs/generated/cozmo.robot.html#cozmo.robot.Robot.pickup_object3
(You pass in the object that you want Cozmo to pickup)."""

"""You can call wait_for_completed later (after you’ve started the actions running in parallel)

E.g:

robot.set_lift_height(1.0).wait_for_completed()
Is the same as writing:

# don't wait yet, just start the action and keep a reference to it
my_lift_action = robot.set_lift_height(1.0)
# ... do any other work you want to do...
# now wait on the action
my_lift_action.wait_for_completed()
So you can do e.g:

# don't wait yet, just start the action and keep a reference to it
my_lift_action = robot.set_lift_height(1.0)
my_head_action = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
# Now that they're both running together in parallel, wait for both of them
my_lift_action.wait_for_completed()
my_head_action.wait_for_completed()
There’s also a helper method wait_for_all_actions_completed:
http://cozmosdk.anki.com/docs/generated/cozmo.robot.html#cozmo.robot.Robot.wait_for_all_actions_completed

so you can simplify the above to just this if you want:

robot.set_lift_height(1.0)
robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
# Now that they're both running together in parallel, wait for everything
robot.wait_for_all_actions_completed()"""

# pickup_object(obj, use_pre_dock_pose=True, in_parallel=False, num_retries=0)

"""Yes - see the documentation here: http://cozmosdk.anki.com/docs/generated/cozmo.robot.html#cozmo.robot.Robot.pickup_object

(You pass in the object that you want Cozmo to pickup)."""

"""import time
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
 robot.drive_straight(distance_mm(200), speed_mmps(50)).wait_for_completed()
cozmo.run_program(cozmo_program)"""

"""robot.play_anim_trigger(cozmo.anim.Triggers.ReactToPokeStartled).wait_for_completed()
 robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail).wait_for_completed()""
"""
"""import cozmo
def cozmo_program(robot: cozmo.robot.Robot):   
    anim = robot.play_anim_trigger(cozmo.anim.Triggers.AudioTestAnim)
    anim.wait_for_completed()
cozmo.run_program(cozmo_program)

anim = robot.play_anim_trigger(cozmo.anim.Triggers.AskToBeRightedRight)
anim.wait_for_completed()"""

"""import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.RollBlock).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.StackBlocks).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.RollBlock).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.StackBlocks).wait_for_completed() 
cozmo.run_program(cozmo_program)"""

"""import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=1000)
    lookaround.stop()
    robot.pickup_object(cubes[0]).wait_for_completed()        
cozmo.run_program(cozmo_program)"""

"""import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()
    robot.pickup_object(cubes[1]).wait_for_completed()
    robot.place_on_object(cubes[2]).wait_for_completed()
cozmo.run_program(cozmo_program)"""

"""import cozmo
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
cozmo.run_program(light) """

"""import cozmo
async def cozmo_program(robot: cozmo.robot.Robot):
    robot.world.disconnect_from_cubes()
cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program)"""


"""import cozmo
async def cozmo_program(robot: cozmo.robot.Robot):
    await robot.world.connect_to_cubes()
cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program)"""

"""has_picked_up_cube = False
# Keep trying the pickup code until successful
while not has_picked_up_cube:
    pickup_action = robot.pickup_object(cube1, num_retries=5)
    pickup_action.wait_for_completed()
    if pickup_action.has_succeeded:
        # Yay - success!
        has_picked_up_cube = True
    else:
        # it failed!
        code, reason = pickup_action.failure_reason
        result = pickup_action.result
        print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
        if not cube1.pose.is_accurate:
            # Cozmo doesn't know exactly where cube1 is - try looking for it again...
            # You'd need to add your own code here to look around until cube1 is found
            pass"""

   """ has_picked_up_cube = False
while not has_picked_up_cube:
    pickup_action = robot.pickup_object(cube1, num_retries=5)
    pickup_action.wait_for_completed()
    if pickup_action.has_succeeded:
        has_picked_up_cube = True
    else:
        code, reason = pickup_action.failure_reason
        result = pickup_action.result
        if not cube1.pose.is_accurate:
            pass


"""cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)
    robot.pickup_object(cube1).wait_for_completed()"""

"""cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)  
robot.pickup_object(cube3).wait_for_completed()"""
 
#  cube1.set_lights(cozmo.lights.white_light)
#  cube1.set_light_corners(light1, light2, light3, light4)
#  cube1.set_light_corners(cozmo.lights.green_light, cozmo.lights.red_light, cozmo.lights.blue_light, cozmo.lights.off_light)
#  cozmo.robot.PickupObject
#  cozmo.robot.PlaceOnObject
#  cozmo.exceptions.NotPickupable
#  cozmo.robot.PlaceObjectOnGroundHere
#  cozmo.exceptions.CannotPlaceObjectsOnThis
#  place_object_on_ground_here(obj, in_parallel=False, num_retries=0)
#  place_on_object(obj, use_pre_dock_pose=True, in_parallel=False, num_retries=0)
#  place_object_on_ground_here(obj, in_parallel=False, num_retries=0)
#  place_object_on_ground_here_factory = functools.partial(<class 'cozmo.robot.PlaceObjectOnGroundHere'>, loop=None)
#  place_on_object_factory = functools.partial(<class 'cozmo.robot.PlaceOnObject'>, loop=None)
#  pickup_object_factory = functools.partial(<class 'cozmo.robot.PickupObject'>, loop=None)
#  pickup_object(obj, use_pre_dock_pose=True, in_parallel=False, num_retries=0)
#  class cozmo.robot.RollCube(obj, approach_angle, check_for_object_on_top, **kw)
#  class cozmo.robot.PickupObject(obj, use_pre_dock_pose=True, **kw)
#  class cozmo.robot.PlaceObjectOnGroundHere(obj, **kw)
#  class cozmo.robot.PlaceOnObject(obj, use_pre_dock_pose=True, **kw)
#  class cozmo.objects.ObservableObject(conn, world, object_id=None, **kw)
#  class cozmo.objects.LightCube(cube_id, *a, **kw)

#  pickup_object()
#  roll_cube()
#  obj = None
#  obj.pickupable
#  obj (cozmo.objects.ObservableObject)
#  use_pre_dock_pose = None

#  descriptive_name
#  object_id
#  cube_id
#  pickupable = False
#  place_objects_on_this = False
#  say_text(text, play_excited_animation=False, use_cozmo_voice=True, duration_scalar=1.0, voice_pitch=0.0, in_parallel=False, num_retries=0)
