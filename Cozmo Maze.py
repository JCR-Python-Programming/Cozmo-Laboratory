import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
 robot.drive_straight(distance_mm(150), speed_mmps(30)).wait_for_completed()
 robot.turn_in_place(degrees(90)) .wait_for_completed()
 robot.drive_straight(distance_mm(280), speed_mmps(30)).wait_for_completed()
 robot.turn_in_place(degrees(180)) .wait_for_completed()
 robot.drive_straight(distance_mm(280), speed_mmps(30)).wait_for_completed()
 robot.turn_in_place(degrees(-90)) .wait_for_completed()
 robot.drive_straight(distance_mm(150), speed_mmps(30)).wait_for_completed()
cozmo.run_program(cozmo_program)
