import asyncio
import time
import cozmo
def light_when_face(robot: cozmo.robot.Robot):
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
    face = None
    while True:
        if face and face.is_visible:
            robot.set_all_backpack_lights(cozmo.lights.blue_light)
        else:
            robot.set_backpack_lights_off()
            try:
                face = robot.world.wait_for_observed_face(timeout=30)
            except asyncio.TimeoutError:
                return
        time.sleep(.1)
cozmo.run_program(light_when_face, use_viewer=True, force_viewer_on_top=True)
