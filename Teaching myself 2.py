import cozmo

def cozmo_program(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()
    if len(cubes) <2:
        print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
    else:
        robot.pickup_object(cubes[0]).wait_for_completed()
        robot.place_on_object(cubes[1]).wait_for_completed()
cozmo.run_program(cozmo_program)
