import sys
import time
try:
    import numpy as np
except ImportError:
    sys.exit("Cannot import numpy: Do `pip3 install --user numpy` to install")
try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")
import cozmo
def get_in_position(robot: cozmo.robot.Robot):
    '''If necessary, Move Cozmo's Head and Lift to make it easy to see Cozmo's face.'''
    if (robot.lift_height.distance_mm > 45) or (robot.head_angle.degrees < 40):
        with robot.perform_off_charger():
            lift_action = robot.set_lift_height(0.0, in_parallel=True)
            head_action = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE,
                                               in_parallel=True)
            lift_action.wait_for_completed()
            head_action.wait_for_completed()
def calc_pixel_threshold(image: Image):    
    grayscale_image = image.convert('L')    
    mean_value = np.mean(grayscale_image.getdata())
    return mean_value
def cozmo_face_mirror(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    get_in_position(robot)
    face_dimensions = cozmo.oled_face.SCREEN_WIDTH, cozmo.oled_face.SCREEN_HALF_HEIGHT
    print("Press CTRL-C to quit")
    while True:
        duration_s =0.1
        latest_image = robot.world.latest_image
        if latest_image is not None:
            # Scale the camera image down to fit on Cozmo's face
            resized_image = latest_image.raw_image.resize(face_dimensions,
                                                          Image.BICUBIC)            
            resized_image = resized_image          
            pixel_threshold = calc_pixel_threshold(resized_image)           
            screen_data = cozmo.oled_face.convert_image_to_screen_data(
                resized_image,
                pixel_threshold=pixel_threshold)            
            robot.display_oled_face_image(screen_data, duration_s * 1000.0)
        time.sleep(duration_s)
cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_face_mirror)
