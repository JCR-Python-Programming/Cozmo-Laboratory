import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Our Father, who art in heaven, hallowed be thy Name, thy kingdom come, thy will be done, on earth as it is in heaven. Give us this day our daily bread. And forgive us our trespasses").wait_for_completed()
    robot.say_text("as we forgive those who trespass against us. And lead us not into temptation, but deliver us from evil. For thine is the kingdom, and the power, and the glory, for ever and ever, in Jesus name. Amen.").wait_for_completed()
cozmo.run_program(cozmo_program)
