import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    # Use a "for loop" to repeat the indented code 4 times
    # Note: the _ variable name can be used when you don't need the value
    for _ in range(8):
        robot.drive_straight(distance_mm(200), speed_mmps(5)).wait_for_completed()
        robot.turn_in_place(degrees(180)) .wait_for_completed()


cozmo.run_program(cozmo_program)
