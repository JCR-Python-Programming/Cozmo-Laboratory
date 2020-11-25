import sys
import time
import cozmo
from PIL import Image
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
 time.sleep(10)
 robot.move_head(-1)
 robot.move_lift(-1)
 time.sleep(5)
 resampling_mode = Image.NEAREST
 image_name= "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Cozmo_Primary_Gradient_Logo-2.png"
 image = Image.open(image_name)
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode) 
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False) 
 duration_s = 3.0 
 robot.display_oled_face_image(face_image, duration_s * 1000.0) 
 time.sleep(duration_s) 
 resampling_mode = Image.NEAREST
 image_name= "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/cozmosdk.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 3.0
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/hello_world.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Cozmo The kid.jpg"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Cozmo The King.jpg"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/ifttt_gmail.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/ifttt_sports.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/ifttt_stocks.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Star-Two-Tone-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Planet-Shape-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Space-Station-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/UFO-Shape-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Alien-Head-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Atom-Shape-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Nuke-Symble-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Round-Squaer-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Squaers-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Hexago-Pattern-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Heart-Shape-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Diamond-Shape-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Club-Shape-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Spade-Shape-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Tittle Mask.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Pure-White-Transparent-Skull-Mask.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Yen-Yan-Shape-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Joey-Tittle-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/3D_Award.jpg"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=True)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Award-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Joey-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Pure-White-Transparent-Portrait.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Mogie-Works-2T.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Youtube Thumbnail.jpg"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Pure-White-Transparent-Dog.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Teardrop-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Spaceuphoria-Logo-Chroma-Ke.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Mascot-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Clear-Website-Link-Card-Mas.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/Spaceuphoria-Link-Chroma-Ke.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 resampling_mode = Image.NEAREST
 image_name = "C:/Users/MI700T/Documents/cozmo_sdk_examples_1.2.1/face_images/The-Joshua-Logo-Chroma-Key.png"
 image = Image.open(image_name)        
 resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)        
 face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,invert_image=False)
 duration_s = 3.0     
 robot.display_oled_face_image(face_image, duration_s * 1000.0)
 time.sleep(duration_s)
 robot.move_head(-1)
 time.sleep(20)
cozmo.run_program(cozmo_program)

#Cozmo The King.jpg
