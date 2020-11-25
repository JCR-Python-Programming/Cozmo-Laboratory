3# Strings are all placed here: These are all what Cozmo will say, before he actually says it. all

speak0=("ha!")
speak00=("alright!")
speak1=("hello world!, my name is Cozmo, I can tell you how many aproximate seconds you have been on earth for, however, I can only tell you your exact birth date to your exact birth date per year.")
speak2=("What is your name, please type your name, then press the enter key to confirm your answer.")
speak3=("nice to meet you {}, my name is cozmo, the robot, I was created and designed by onkie incorporated.")
speak4=("{}, I can do a lot with some powerful python programming skills, like these sdk python program examples my master created for other devoted cozmo tweakers!")
speak5=("how are you doing {}, please type g if you feel good, or type b if you feel bad, then press the enter key to confirm your answer.")
speak6=("Alright!")
speak7=("{}, that's excellent, it's so good to hear that!")
speak8=("awe!")
speak9=("i'm so very sorry to hear that {}, but chin up, things always have a strange way of working out!")
speak10=("{}, how old are you, please type your age, then press the enter key to confirm your answer.")
speak11=("{}, you are {} years old, happy birthday to you, now, let's find out just how many aproximate seconds you have been on earth for!")
speak12=("your aproximate time on earth in weeks is {} weeks.")
speak120=("your aproximate time on earth in days is {} days.")
speak13=("{}, your aproximate time on earth in months is {} months,")
speak14=("your aproximate time on earth in hours is {} hours.")
speak140=("your aproximate time on earth in minutes is {} minutes")
speak15=("and finally, your aproximate time on earth in seconds is {} seconds")
speak16=("{}, what is your favorite colour, please type your favorite colour, then press the enter key to confirm your answer.")
speak17=("{}, black is not a colour, but it is very popular all the same, black also hides dust and dirt very well.")
speak18=("{}, white is not a colour, but it is very popular at wedings, however, it doesn't hide dust and dirt very well.")
speak19=("{}, sky blue, and dark, navey blue are very popular colours, good choice!")
speak20=("{}, candy apple red is an awesome colour for a sports car, excellent choice!")
speak21=("{}, green is one of the most widely used holiday festive colours next to red, and green is so lean, never mean, it's a joke, get it?")
speak22=("{}, yellow is as bright as the sun, and it's so mellow, it's a joke, get it?")
speak23=("{}, pink often reminds us of soft peddles atop of a flower on a warm, calm, and sunny day.")
speak24=("{}, orange you glad you learned python, it's a joke, get it?")
speak25=("{}, don't ever let anyone give you a purple nurple, I hear they hurt a lot, lucky i'm only a simple plastic robot, because I never, ever want purple nurples, it's a joke, get it?")
speak26=("{}, electric cyan is my most favorite of all the colours in the whole wide world, it's such an awesome choice!")
speak27=("{}, silver is also one of my favorite colours next to cyan, but for shine and sheen, I just love bright, and shiny chrome the most!")
speak28=("{}, Gold is such a prestigious metal ore, did you know you can eat gold?")
speak29=("{}, what would be your favorite kind of pet, if you get one, please type your favorite kind of pet, then press the enter key to confirm your answer.")
speak30=("{}, dogs are very loyal, and they are widely considered to be man's best friend, dogs are also known to protect their owners, with their lives")
speak31=("{}, cats are cool, they are very crafty, stealthy, and very clever on their own, like the old saying goes, cats own you, you don't own cats")
speak32=("{}, birds are so much fun to keep as pets, they can entertain you for hours on end.")
speak33=("{}, fish are so relaxing to watch, especially inside a huge, cystal clear aquarium.")
speak34=("{}, having a pet mouse around the house is a great pet for children, who are learnig how to take care of a pet for the very first time, and they are very cost efficient to keep as pets as well.")
speak35=("{}, rats are very inteligent animals, and they are great to keep as pets, and like a pet mouse, rats are also cost efficient to keep as pets")
speak36=("{}, some species of turtles can live for hundreds of years, imagine that!")
speak37=("{}, hamsters use their cheeks to store lots of uneaten food away, they run non stop, all night long on a hamster wheel!")
speak38=("{}, did you know that monkeys are the closest animal primate species, next to the human animal primate species?")
speak39=("well {}, it's been really nice chatting about with you, however, i don't want to over visit and wear out my warm welcome!")
speak40=("but please keep learning python to truly unleash the robust robot inside cozmo, and most important of all, have fun, and use your imagination, you just never know where it will take you!")
INCOR1=("that is incorrect, please try again!")
INCOR2=("that is incorrect, please type in numbers only!")
INCOR3=("now you are just messing about with me, if you do that again, I will quit playing!")
INCOR4=("that's it, i quit!")
animation_function=("anim_poked_giggle"); key1=("g"); key2=("b")

# Strings and tuples are great to use, because they help in speeding up tedious programming time.
INCOR= (INCOR1,INCOR2,INCOR3,INCOR4)

pet0=("dog"); pet1=("cat"); pet2=("bird"); pet3=("fish"); pet4=("mouse"); pet5=("rat"); pet6=("turtle"); pet7=("hamster"); pet8=("monkey")

# Some more strings:

choose_colour0=("black"); choose_colour1=("white"); choose_colour2=("blue"); choose_colour3=("red"); choose_colour4=("green"); choose_colour5=("yellow")
choose_colour6=("pink"); choose_colour7=("orange"); choose_colour8=("purple"); choose_colour9=("cyan"); choose_colour10=("silver"); choose_colour11=("gold")

# Executable Code, using the exec(Redundant_Code) You can name the exec any name you like, but you must have the exec function in place, before the first bracket.

Redundant_Code = '''
robot.play_anim(name="anim_poked_giggle").wait_for_completed()
robot.play_anim(name="anim_poked_giggle").wait_for_completed()
robot.play_anim(name="anim_poked_giggle").wait_for_completed()
robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
'''
import cozmo
import time
def cozmo_program(robot: cozmo.robot.Robot):

     robot.say_text(speak0,play_excited_animation=True).wait_for_completed()
     robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
     robot.say_text(speak1).wait_for_completed()

     name=input(robot.say_text(speak2).wait_for_completed())
     robot.say_text(speak3.format(name)).wait_for_completed()
     robot.say_text(speak4.format(name)).wait_for_completed()
     ask=input(robot.say_text(speak5.format(name)).wait_for_completed())

     if ask == str(key1): # G for good
               robot.say_text(speak6,play_excited_animation=True).wait_for_completed()
               robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
               robot.say_text(speak7.format(name)).wait_for_completed()
               
               # input age speak10 how old are you
               age=input(robot.say_text(speak10.format(name)).wait_for_completed())
                
     elif ask == str(key2): # B for bad
               robot.say_text(speak8,play_excited_animation=True).wait_for_completed()
               robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
              robot.say_text(speak9.format(name)).wait_for_completed()

               # input age speak10 how old are you
               age=input(robot.say_text(speak10.format(name)).wait_for_completed())
     for i in range(4):     
      if age>=str("A") or age<=("/") or age>=("=") or age>=("<") or age>=(">"):
               age=input(robot.say_text(INCOR[i]).wait_for_completed())             
      else:
               robot.say_text(speak11.format(name,age)).wait_for_completed()
               break
      
     age=input(robot.say_text(speak10.format(name)).wait_for_completed())

       # robot.say {}, you are {} years old, happy birthday to you
     robot.say_text(speak11.format(name,age)).wait_for_completed()

     # Strings and Tuples can also go onto one single line, just as you notice here:

     mult1 = int(age)*365; mult2 = int(age)*52; mult3 = int(age)*12; mult4 = int(age)*365*24; mult5 = int(age)*360*24*60; mult6 = int(age)*360*24*60*60;int(age) >=1

     robot.say_text(speak13.format(name,mult3)).wait_for_completed()
     robot.say_text(speak12.format(mult2)).wait_for_completed()
     robot.say_text(speak120.format(mult1)).wait_for_completed()
     robot.say_text(speak14.format(mult4)).wait_for_completed()
     robot.say_text(speak140.format(mult5)).wait_for_completed()
     robot.say_text(speak15.format(mult6)).wait_for_completed()

     colour = input(robot.say_text(speak16.format(name)).wait_for_completed())

     if colour == str(choose_colour0):
               robot.say_text(speak17.format(name)).wait_for_completed()

     elif colour == str(choose_colour1):
              robot.say_text(speak18.format(name)).wait_for_completed()

     elif colour == str(choose_colour2):
               robot.say_text(speak19.format(name)).wait_for_completed()

     elif colour == str(choose_colour3):
               robot.say_text(speak20.format(name)).wait_for_completed()

     elif colour == str(choose_colour4):
               robot.say_text(speak21.format(name)).wait_for_completed()

               exec(Redundant_Code)

               robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

     elif colour == str(choose_colour5):
               robot.say_text(speak22.format(name)).wait_for_completed()

              # Here is a great example of what the exec function can do. exec functions are great for holding redundant commands,
              # you need, but don't want to have to rewrite them over and oever again.
              # exec fuction generators can hold complex codes, which allow you to use only one redundant line of code:

               exec(Redundant_Code)

     elif colour == str(choose_colour6):
               robot.say_text(speak23.format(name)).wait_for_completed()

     elif colour == str(choose_colour7):
               robot.say_text(speak24.format(name)).wait_for_completed()

               exec(Redundant_Code)

     elif colour == str(choose_colour8):
               robot.say_text(speak25.format(name)).wait_for_completed()

               exec(Redundant_Code)

     elif colour == str(choose_colour9):
               robot.say_text(speak0,play_excited_animation=True).wait_for_completed()
               robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
               robot.say_text(speak26).wait_for_completed()
               robot.play_anim(name=animation_function).wait_for_completed()
               robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

     elif colour == str(choose_colour10):
               robot.say_text(speak27.format(name)).wait_for_completed()

     elif colour == str(choose_colour11):
               robot.say_text(speak28.format(name)).wait_for_completed()

     pet=input(robot.say_text(speak29.format(name)).wait_for_completed())

     if pet == str(pet0):
               robot.say_text(speak30.format(name)).wait_for_completed()

     elif pet == str(pet1):
               robot.say_text(speak31.format(name)).wait_for_completed()
               robot.play_anim(name=animation_function).wait_for_completed()
               robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

     elif pet == str(pet2):
               robot.say_text(speak32.format(name)).wait_for_completed()

     elif pet == str(pet3):
               robot.say_text(speak33.format(name)).wait_for_completed()

     elif pet == str(pet4):
               robot.say_text(speak34.format(name)).wait_for_completed()

     elif pet == str(pet5):
               robot.say_text(speak35.format(name)).wait_for_completed()

     elif pet == str(pet6):
               robot.say_text(speak36.format(name)).wait_for_completed()
               robot.play_anim_trigger(cozmo.anim.Triggers.BouncerRequestToPlay).wait_for_completed()

     elif pet == str(pet7):
               robot.say_text(speak37.format(name)).wait_for_completed()

     elif pet == str(pet8):
               robot.say_text(speak38.format(name)).wait_for_completed()

     robot.say_text(speak00.format(name),play_excited_animation=True).wait_for_completed()
     robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
     robot.say_text(speak39.format(name)).wait_for_completed()
     robot.say_text(speak40).wait_for_completed()

cozmo.run_program(cozmo_program, use_viewer=False)
