import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
    for i in range(9):    
        robot.say_text(str(9-i)).wait_for_completed()
cozmo.run_program(cozmo_program)
