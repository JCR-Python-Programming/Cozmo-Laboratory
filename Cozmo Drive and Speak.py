import cozmo

def cozmo_program(robot: cozmo.robot.Robot):
    from cozmo.util import degrees, distance_mm, speed_mmps
    for _ in range(4):
        robot.drive_straight(distance_mm(200), speed_mmps(20)).wait_for_completed()
        robot.turn_in_place(degrees(180)) .wait_for_completed()
        robot.say_text("Error! Error! Exterminait! Exterminait! Exterminait! Error! Error!").wait_for_completed()
cozmo.run_program(cozmo_program)
