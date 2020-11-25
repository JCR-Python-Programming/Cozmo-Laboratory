import cozmo
from cozmo.util import degrees
def cozmo_program(robot: cozmo.robot.Robot):
    robot.turn_in_place(degrees(90)).wait_for_completed()
    anim = robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin)
    anim.wait_for_completed()
cozmo.run_program(cozmo_program)
