import cozmo
def cozmo_program(robot: cozmo.robot.Robot):    
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession, ignore_body_track=True).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession, ignore_body_track=True).wait_for_completed()
cozmo.run_program(cozmo_program)

