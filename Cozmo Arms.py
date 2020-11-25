import cozmo
import time
def cozmo_program(robot: cozmo.robot.Robot):
    robot.drive_wheels(30,30)
    robot.move_lift(1)    
    time.sleep(10)
    robot.move_head(-90)
cozmo.run_program(cozmo_program)
