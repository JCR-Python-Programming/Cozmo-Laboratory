import time
import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.start_behavior(cozmo.behavior.BehaviorTypes.StackBlocks).wait_for_completed()
cozmo.run_program(cozmo_program)
