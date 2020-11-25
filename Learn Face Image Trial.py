import sys
import time
import cozmo
from PIL import Image
def cozmo_program(robot: cozmo.robot.Robot):
 resampling_mode = Image.NEAREST
 image_name= "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/hello_world.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 2.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Cozmo The kid.jpg"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 2.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
cozmo.run_program(cozmo_program)
