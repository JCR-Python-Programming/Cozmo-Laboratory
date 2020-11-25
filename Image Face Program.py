import sys
import time
import cozmo
from PIL import Image
def cozmo_program(robot: cozmo.robot.Robot):    
    robot.move_head(-1)
    robot.move_lift(-1)
    time.sleep(10)
    robot.move_head(1)
    time.sleep(.4)
    robot.play_anim(name="id_poked_giggle").wait_for_completed()
    robot.play_anim(name="id_poked_giggle").wait_for_completed()
    robot.play_anim(name="id_poked_giggle").wait_for_completed()
    image_settings = [("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/cozmosdk.png", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Cozmo The kid.jpg", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Cozmo The King.jpg", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/hello_world.png", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/ifttt_gmail.png", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/ifttt_sports.png", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/ifttt_stocks.png", Image.NEAREST),                      
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Glowing_Alien_Authorize.jpg", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Glowing_Geo-Sphere.jpg", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/White-Website-Link-Card.png", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Joey-in-Lights-Web-Small.gif", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Joey-Chroma-Key.png", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/3D_Award.jpg", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Pure-White-Transparent-Portrait.png", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Mogie-Works-2T.png", Image.NEAREST),
                      ("C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Pure-White-Transparent-Dog.png", Image.NEAREST),]    
    face_images = []
    for image_name, resampling_mode in image_settings:
        image = Image.open(image_name)        
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
        face_images.append(face_image)   
    num_loops = 1
    duration_s = 2.0     
    for _ in range(num_loops):
        for image in face_images:
            robot.display_oled_face_image(image, duration_s * 1000.0)
            time.sleep(duration_s)
cozmo.run_program(cozmo_program)
def cozmo_program(robot: cozmo.robot.Robot): 
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 robot.play_anim(name="id_poked_giggle").wait_for_completed()
 robot.move_head(1)
 robot.move_lift(1)
 time.sleep(1)
 robot.move_lift(-1)
 time.sleep(1)
cozmo.run_program(cozmo_program)

#face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
