
import time
person_found = False
marker_found = False

def scan_for_marker():# Turn on detection and scan left and right until you hit a marker.
        global marker_found
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        marker_found = Falsegimbal_ctrl.yaw_ctrl(-90)
        while marker_found == False:
            gimbal_ctrl.yaw_ctrl(+180)
            gimbal_ctrl.yaw_ctrl(-180)


def vision_recognized_people(msg):
    global person_found

    media_ctrl.play_sound(rm_define.media_sound_recognize_success)

    vision_ctrl.disable_detection(rm_define.vision_detection_people)

    led_ctrl.gun_led_off()

    gimbal_ctrl.set_rotate_speed(540)


    gimbal_ctrl.pitch_ctrl(25)

    gimbal_ctrl.pitch_ctrl(0)

    gimbal_ctrl.pitch_ctrl(25)

    gimbal_ctrl.pitch_ctrl(0)

    gimbal_ctrl.pitch_ctrl(25)

    gimbal_ctrl.pitch_ctrl(0)

    gimbal_ctrl.pitch_ctrl(25)

    gimbal_ctrl.pitch_ctrl(0)

    gimbal_ctrl.set_rotate_speed(45)

    person_found = True


def scan_for_person_and_play_sound():
    global person_found

    vision_ctrl.enable_detection(rm_define.vision_detection_people)

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 150, 0, rm_define.effect_breath)

    led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 255, 10, 0, rm_define.effect_always_on)

    led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 10, 0, rm_define.effect_always_on)

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 150, 0, rm_define.effect_breath)

    person_found = False

    while person_found == False:
        media_ctrl.play_sound(rm_define.media_sound_scanning)

        gimbal_ctrl.set_rotate_speed(10)

        led_ctrl.gun_led_on()

        gimbal_ctrl.pitch_ctrl(10)

        gimbal_ctrl.yaw_ctrl(-180)

        gimbal_ctrl.yaw_ctrl(180)

def vision_recognized_marker_letter_F(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    marker_found = True

#def start():robot_ctrl.set_mode(rm_define.robot_mode_free)
# Move the robot to within 1 meter of the marker.chassis_ctrl.
# move_with_distance(0,1.4)
# chassis_ctrl.rotate_with_degree(rm_define.aniticlockwise, 90)
# chassis_ctrl.move_with_distance(0,.6)# Scan for a marker.
# This function is set up before the start().scan_for_marker()

def start():
    roomone = 1 #or Fire
    roomtwo = 2 #or skip
    roomthree = 1 #or fire
    roomfour = 3 #or Person


    #controls robot
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    #set the speed for robot
    chassis_ctrl.set_trans_speed(0.8)
    #Moves the robot a specific  distance (4.68 meters)
    chassis_ctrl.move_with_distance(0, 4.68)
    gimbal_ctrl.recenter()


    chassis_ctrl.move_with_distance(0, 2.56)
    gimbal_ctrl.recenter()
    #brings robot up to door

    chassis_ctrl.set_rotate_speed(30)

    #rotates robot into the first room
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    #move rebot into room for fire


    chassis_ctrl.move_with_distance(0, 4.70)

    scan_for_marker()
#if scan_for_person_and_play_sound()
    gimbal_ctrl.recenter()


    #Robot leaves room and gets back on track
    chassis_ctrl.move_with_distance(180, 4.70)

#IF hostage


    #robot rotates back on track
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
#if hostage
    #chassis_ctrl.move_with_distance(0, 4.68)
    #gimbal_ctrl.recenter()
    #chassis_ctrl.move_with_distance(0, 2.56)
    # chassis_ctrl.move_with_distance(180, 4.68)
    # gimbal_ctrl.recenter()
    # chassis_ctrl.move_with_distance(180, 2.56)

    #robot continues to the turn
    chassis_ctrl.move_with_distance(180, 4.93)
    chassis_ctrl.move_with_distance(180, 2.59)

    #turn robot 45 degrees move 271 the straightin
    chassis_ctrl.move_with_distance(135, 2.71)

    #sleeps for 5 seconds on the mark
    time.sleep(5)
    #proceed straigt to the 2ed door confirm its posion
    #proceeds to next room

    chassis_ctrl.move_with_distance(0, 4.00)
    chassis_ctrl.move_with_distance(0, 1.52)


    #check room 2, make sure its posion
    led_ctrl.gun_led_on()
    gimbal_ctrl.recenter()
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    led_ctrl.gun_led_off()
   #move on to next room 3
    chassis_ctrl.move_with_distance(0, 1.76)
    chassis_ctrl.move_with_distance(0, 3.90)
    chassis_ctrl.move_with_distance(0, 2.84)
    #turns to move into room 3
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 3.45)
    chassis_ctrl.move_with_distance(90, 1.45)
    chassis_ctrl.move_with_distance(0, 3.60)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    #Scan Hostage
    gimbal_ctrl.set_rotate_speed(45)
    chassis_ctrl.set_trans_speed(0.5)
    chassis_ctrl.set_rotate_speed(60)
    scan_for_person_and_play_sound()
    #scan_for_person()

    #makes it to hostage
    #RETURN TO START
#IF FIRE
    #scan_for_person_and_play_sound()
    #leave room
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 3.60)
    chassis_ctrl.move_with_distance(90, 1.45) #goes wring direction
    chassis_ctrl.move_with_distance(0, 3.45)






    #Now exit room , back on path to start
#IF FIRE
#   chassis_ctrl.move_with_distance(0, 5.00)
#   chassis_ctrl.move_with_distance(0, 5.00)
#   chassis_ctrl.move_with_distance(0, 0.29)
    #skip to room 4
#IFFIRE
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 4.00)
    chassis_ctrl.move_with_distance(0, 1.52)
    chassis_ctrl.move_with_distance(0, 3.47)
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 0.20)

    time.sleep(5)
    #reachs the 45 degree turn

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 38)
    chassis_ctrl.move_with_distance(0, 2.68)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 51)

    #^^^^^^^test might work might not

    #need to figure out orintation of bot to straightin out

    #rotate 90 cw ????? may remove depends on results
    #continue down hall to start point


    chassis_ctrl.move_with_distance(0, 4.93)
    chassis_ctrl.move_with_distance(0, 4.68)
    chassis_ctrl.move_with_distance(0, 2.59)
    chassis_ctrl.move_with_distance(0, 2.56)

    # turn around to begin the course over again
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)


    #return down hall to turn!

    chassis_ctrl.move_with_distance(0, 4.93)
    chassis_ctrl.move_with_distance(0, 4.68)
    chassis_ctrl.move_with_distance(0, 2.59)
    chassis_ctrl.move_with_distance(0, 2.56)

    #make it around turn SHOULD WORKN LOL
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 38)
    chassis_ctrl.move_with_distance(0, 2.68)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 51)

    #idk idk we get get the time sleep or not for the second turn
    #so i  am gong to add both for now


    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
    time.sleep(5)

    #continue down hall to room 4!
    chassis_ctrl.move_with_distance(0, 4.04)
    chassis_ctrl.move_with_distance(0, 1.00)
    chassis_ctrl.move_with_distance(0, 3.73)
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 0.29)

    #enters forth room

    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 2.10)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 2.10)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    #scan function
    scan_for_marker()
#if Hostage
    #leave room
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 2.10)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 2.10)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    #back to start CODE

    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 5.00)
    chassis_ctrl.move_with_distance(0, 0.29)
    chassis_ctrl.move_with_distance(0, 4.00)
    chassis_ctrl.move_with_distance(0, 1.73)
    chassis_ctrl.move_with_distance(0, 5.00)

    #makes it to turn
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 38)
    chassis_ctrl.move_with_distance(0, 2.68)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 51)

    #turns to starting hall way
    chassis_ctrl.move_with_distance(0, 4.93)
    chassis_ctrl.move_with_distance(0, 4.68)
    chassis_ctrl.move_with_distance(0, 2.59)
    chassis_ctrl.move_with_distance(0, 2.56)


    #reach Start Point









