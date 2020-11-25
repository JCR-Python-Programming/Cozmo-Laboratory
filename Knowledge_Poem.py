import time
import cozmo
def cozmo_program(robot: cozmo.robot.Robot): 
 time.sleep(10)
 robot.say_text("Knowledge is a free invention of the heart and of the mind itself! The only textbooks needed, are the heart and the mind. The only exam to be written is the key to ponder into wonder.").wait_for_completed()
 robot.say_text("For the heart and the mind hold the key to the greatest diploma of all, the dream’s creation of our imagination, For the heart and the mind are thus the greatest teachers of us. Believe in yourself! For you are their greatest student.").wait_for_completed()
 robot.say_text("THIS BELONGS TO EVERY MAN, WOMAN AND CHILD, Never give up your dream, no matter how far away it may seem to be, because that is when it is ever so close to becoming true.").wait_for_completed()
 robot.say_text("If you dream of something long enough and strong enough, your dream will come true, when you least expect it, Always remember, we are never too young or too old to dream and use our imagination.").wait_for_completed()
 robot.say_text("for we only get one, and it is ours forever, May your heart be filled with courage and compassion, and your mind be as limitless and as wondrous as the universe itself!, If you dream it, you can be it. Believe it!").wait_for_completed()
 time.sleep(10)
cozmo.run_program(cozmo_program)
