import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 robot.play_anim(name= "id_poked_giggle").wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.RollBlock).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.StackBlocks).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.RollBlock).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).wait_for_completed()
 robot.start_behavior(cozmo.behavior.BehaviorTypes.StackBlocks).wait_for_completed() 
cozmo.run_program(cozmo_program)

