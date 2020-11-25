import asyncio
import time

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def drive_to_charger(robot):
    '''The core of the drive_to_charger program'''

    # If the robot was on the charger, drive them forward and clear of the charger
    if robot.is_on_charger:
        # drive off the charger
        robot.drive_off_charger_contacts().wait_for_completed()
        robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
        # Start moving the lift down
        robot.move_lift(-3)
        # turn around to look at the charger
        robot.turn_in_place(degrees(180)).wait_for_completed()
        # Tilt the head to be level
        robot.set_head_angle(degrees(0)).wait_for_completed()
        # wait half a second to ensure Cozmo has seen the charger
        time.sleep(0.5)
        # drive backwards away from the charger
        robot.drive_straight(distance_mm(-60), speed_mmps(50)).wait_for_completed()

    # try to find the charger
    charger = None

    # see if Cozmo already knows where the charger is
    if robot.world.charger:
        if robot.world.charger.pose.is_comparable(robot.pose):
            print("Cozmo already knows where the charger is!")
            charger = robot.world.charger
        else:
            # Cozmo knows about the charger, but the pose is not based on the
            # same origin as the robot (e.g. the robot was moved since seeing
            # the charger) so try to look for the charger first
            pass

    if not charger:
        # Tell Cozmo to look around for the charger
        look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        try:
            charger = robot.world.wait_for_observed_charger(timeout=30)
            print("Found charger: %s" % charger)
        except asyncio.TimeoutError:
            print("Didn't see the charger")
        finally:
            # whether we find it or not, we want to stop the behavior
            look_around.stop()

    if charger:
        # Attempt to drive near to the charger, and then stop.
        action = robot.go_to_object(charger, distance_mm(65.0))
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")


cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on charger for now
cozmo.run_program(drive_to_charger, use_viewer=True, force_viewer_on_top=True)
