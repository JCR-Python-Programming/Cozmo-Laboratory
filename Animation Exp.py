import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.set_head_light(True)
 robot.say_text("yeah, I did it!", play_excited_animation=True).wait_for_completed()
cozmo.run_program(cozmo_program)

"""
mport cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):

anim = robot.play_anim_trigger(cozmo.anim.Triggers.AskToBeRightedRight)
anim.wait_for_completed()
"""
# robot.play_anim_trigger(cozmo.anim.Triggers.AudioTestAnim).wait_for_completed()
# robot.play_anim_trigger(cozmo.anim.Triggers.AskToBeRightedRight).wait_for_completed()
# robot.play_anim_trigger(cozmo.anim.Triggers.AskToBeRightedLeft).wait_for_completed()
# robot.play_anim_trigger(cozmo.anim.Triggers.AcknowledgeObject).wait_for_completed()
# robot.play_anim_trigger(cozmo.anim.Triggers.AcknowledgeFaceInitPause).wait_for_completed()

# robot.say_text("I'm so happy today", play_excited_animation=True).wait_for_completed() 
# "I'm so happy today"


# go_to_object(target_object, distance_from_object, in_parallel=False, num_retries=0)
#go_to_pose(pose, relative_to_robot=False, in_parallel=False, num_retries=0)
#go_to_object_factory = functools.partial(<class 'cozmo.robot.GoToObject'>, loop=None)

# (cozmo.objects.ObservableObject)
# (cozmo.util.Distance)
# cozmo.util.Distance(distance_mm=None, distance_inches=None)
# cozmo.robot.GoToObject
# go_to_object()
# set_head_light(enable)
