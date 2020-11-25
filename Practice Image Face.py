import sys
import time
import cozmo
from PIL import Image
from cozmo.util import degrees, distance_mm, speed_mmps
def setup_position(robot: cozmo.robot.Robot):
 if robot.lift_height.distance_mm > 45:
    with robot.perform_off_charger():
       robot.set_lift_height(0,20).wait_for_completed()
 resampling_mode = Image.NEAREST
 image_name= "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Cozmo_Primary_Gradient_Logo-2.png"
 image = Image.open(image_name)
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode) 
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False) 
 duration_s = 3.0 
 robot.display_oled_face_image(face_image, duration_s * 1000.0) 
 time.sleep(duration_s)
cozmo.run_program(setup_position)
