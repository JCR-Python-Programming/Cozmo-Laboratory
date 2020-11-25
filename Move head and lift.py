import cozmo
import time
def cozmo_program(robot: cozmo.robot.Robot):
 robot.move_head(2)
 robot.move_lift(1)
 time.sleep(1)
 robot.move_head(-1)
 robot.move_lift(-1)
 time.sleep(1)
 robot.set_lift_height(0,1).wait_for_completed()
 time.sleep(1)
cozmo.run_program(cozmo_program)
