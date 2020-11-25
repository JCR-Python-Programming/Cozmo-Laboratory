import cozmo
def cozmo_program(robot: cozmo.robot.Robot):
 from cozmo.util import degrees, Pose, distance_mm, speed_mmps
 from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
 cube1 = robot.world.get_light_cube(LightCube1Id)
 cube2 = robot.world.get_light_cube(LightCube2Id)
 cube3 = robot.world.get_light_cube(LightCube3Id)

 lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
 robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=60)
 lookaround.stop()
 robot.go_to_object(cube2, distance_mm(120)).wait_for_completed()
 robot.roll_cube(cube2, check_for_object_on_top=True, num_retries=9).wait_for_completed()
     
cozmo.run_program(cozmo_program)

#robot.go_to_object(cube, distance_mm(70.0)).wait_for_completed()
# robot.roll_cube(cube1, check_for_object_on_top=True, num_retries=2).wait_for_completed()
# robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=60)
# lookaround.stop()
# lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace) 
# robot.pickup_object(cube1,use_pre_dock_pose=True, in_parallel=True, num_retries=5).wait_for_completed()
