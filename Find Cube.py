import cozmo
import time
def cozmo_program(robot: cozmo.robot.Robot):
    cube = None
    get_in_position(robot)
    drow(robot)
    imagex(robot)
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=60)
    except asyncio.TimeoutError:
        print("Didn't find a cube :-(")
        return
    finally:
        look_around.stop()

    cube.start_light_chaser()
    try:
        print("Waiting for cube to be tapped")
        cube.wait_for_tap(timeout=10)
        print("Cube tapped")
      
    except asyncio.TimeoutError:
        print("No-one tapped our cube :-(")
    finally:
        cube.stop_light_chaser()
        cube.set_lights_off()
    # Play an animation via its Name.
    # Warning: Future versions of the app might change these, so for future-proofing
    # we recommend using play_anim_trigger above instead.
    # See the remote_control_cozmo.py example in apps for an easy way to see
    # the available animations.
    robot.play_anim(name="ID_pokedB").wait_for_completed()
