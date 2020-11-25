import sys
import time
import cozmo
from PIL import Image
def cozmo_program(robot: cozmo.robot.Robot):
 face_image = Image.open("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Recorded Energy Power Cell Drawing EX 2.jpg")
 face_image = face_image.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)
 face_image = cozmo.oled_face.convert_image_to_screen_data(face_image,
                                                           invert_image=True)
time.sleep(7)
cozmo.run_program(cozmo_program)

#BICUBIC)
#NEAREST)
