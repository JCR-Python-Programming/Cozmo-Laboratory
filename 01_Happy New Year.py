import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.say_text("Happy New Year 2018. See!, even robots of all shapes and sizes love to party just as much as our human counterparts love to party, especially on New Years eve!").wait_for_completed()
 robot.say_text("Please drink responsibly. Don't drink and drive. Arrive alive! A message from cozmo, the robot. ").wait_for_completed()
cozmo.run_program(cozmo_program)
