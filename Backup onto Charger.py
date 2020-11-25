import time
import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.backup_onto_charger(max_drive_time=3)
cozmo.run_program(cozmo_program)
