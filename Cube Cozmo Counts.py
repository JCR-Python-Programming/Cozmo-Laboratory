import cozmo
import time
def cozmo_program(robot: cozmo.robot.Robot):
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
    for i in range(5):
        robot.say_text("Power Cube").wait_for_completed()
        robot.move_lift(3)
        robot.say_text(str(i+0).wait_for_completed()
        robot.move_lift(-3)
        time.sleep(1)
cozmo.run_program(cozmo_program)
