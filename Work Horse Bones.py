Redundant_Code = '''
robot.play_anim(name="anim_poked_giggle").wait_for_completed()
robot.play_anim(name="anim_poked_giggle").wait_for_completed()
robot.play_anim(name="anim_poked_giggle").wait_for_completed()
robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
'''
import cozmo
import time
def cozmo_program(robot: cozmo.robot.Robot):
 robot.say_text(" hah",play_excited_animation=True).wait_for_completed()
 robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
 
 robot.say_text("hello world!, my name is Cozmo, I can tell you how many aproximate seconds you have been on earth for, however, I can only tell you your exact birth date to your exact birth date per year.").wait_for_completed() 
 
 name=input(robot.say_text("What is your name, please type your name, then press the enter key to confirm your answer.").wait_for_completed())
 robot.say_text("nice to meet you {}, my name is cozmo, the robot, I was created and designed by onkie incorporated".format(name)).wait_for_completed()
 robot.say_text("{}, I can do a lot with some powerful python programming skills, like these sdk python program examples my master created for other devoted cozmo tweakers!".format(name)).wait_for_completed()
 while True:
  ask=input(robot.say_text("how are you doing {}, to answer my question, please type g if you feel good, or type b if you feel bad, then press the enter key to confirm your answer.".format(name)).wait_for_completed())

  if ask == str("g"):           
           robot.say_text("{}, that's excellent, it's so good to hear that!".format(name)).wait_for_completed()
  elif ask >= str("A"):      
           robot.say_text("incorrect response {}, please try again!".format(name)).wait_for_completed()
           continue
  elif ask == str("b"):
           robot.say_text("awe",play_excited_animation=True).wait_for_completed()
           robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
           robot.say_text("i'm so very sorry to hear that {}, but chin up, things always have a strange way of working out!").wait_for_completed()
           break
cozmo.run_program(cozmo_program, use_viewer=False)


"""
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if age >= 18: 
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")
"""
