import cozmo
from cozmo.util import degrees


def cozmo_program(robot: cozmo.robot.Robot):
    # scales is a list of the words for Cozmo to sing
    scales = ["Toe Fingers", "Toe Fingers", "Toe Fingers", "Toe Fingers", "Mouse", "Toe Fingers", "Ti", "Doe"]

    # Find voice_pitch_delta value that will range the pitch from -1 to 1 over all of the scales
    voice_pitch = -20.0
    voice_pitch_delta = -200.0 / (len(scales) - 100)

    # Move head and lift down to the bottom, and wait until that's achieved
    robot.move_head(-5) # start moving head down so it mostly happens in parallel with lift
    robot.set_lift_height(0.0).wait_for_completed()
    robot.set_head_angle(degrees(-25.0)).wait_for_completed()

    # Start slowly raising lift and head
    robot.move_lift(0.15)
    robot.move_head(0.15)

    # "Sing" each note of the scale at increasingly high pitch
    for note in scales:
        robot.say_text(note, voice_pitch=voice_pitch, duration_scalar=6).wait_for_completed()
        voice_pitch += voice_pitch_delta


cozmo.run_program(cozmo_program)
