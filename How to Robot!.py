
def start()
    roomone = 1 or Fire
    roomtwo = 2 or skip
    roomthree = 1 or fire
    roomfour = 3 or Person


def start():
    #This must be the first line of any module that your write.
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    #Set Rotate Speed: This set speed of the Gimble
    gimbal_ctrl.set_rotate_speed(60)

    ## Yaw_ctrl rotates the gimbal by the number of degrees you pass into the function.
    # In this case, 250.

    gimbal_ctrl.yaw_ctrl(250)

    # Likewise, pitch_ctrl rotates the gimbal up and down by the number of degrees
    # specified, in this case 15.

    gimbal_ctrl.pitch_ctrl(15)

    # Recenter always rotates the gimbal back to its starting position of staring directly
    # forward in front of it (yaw-wise), with a level pitch. Basically, it reset to 0, 0.

    gimbal_ctrl.recenter()

    # This next line sets the rotation speed for the bot itself rotating around
    # using it's wheels.

    chassis_ctrl.set_rotate_speed(30)

    # Rotate with degree takes in a direction of rotation, and a number of degrees for
    # the bot to rotate.

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    # set_trans_speed sets the movement speed of the robot in meters per second

    chassis_ctrl.set_trans_speed(0.5)

    # move_with_distance takes in two parameters, the first is an angle (0 meaning
    # move straight ahead forward), and the second is a distance in meters (in this case,
    # move 0.3 meters forward – the max distance is 5 meters - if you need to move
    # more than 5 meters you need to set up two – or more – commands.)

    chassis_ctrl.move_with_distance(0, 0.3)
    gimbal_ctrl.recenter()

# How to make a robot enter a room with python! EXAMPLE
def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    #move to door
    chassis_ctrl.move_with_distance(0,3.5)

    #Rotate to face door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90);

    #Drive Through Door
    chassis_ctrl.move_with_distance(0,1)

    if(roomone == 1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        scan_for_fire()

    #Notice the last line line of code "Scan for Fire" will need to create a function
    #to detect the room
    # function is called by the system and executed
#automatically. If there are a possibility of multiple markers,
# you would set up the function
#for each. In this case we have just    set up for the letter F in each room.

    #Along with marker recognition you will also be required to recognize
# people for a room
#type of 3. The code for person recognition is very similar to marker recognition.
# As noted
#previously I would
# replace lines 30 and 32 with gimbal_ctrl.yaw_ctrl(degrees) comman

def vision_people(msg):
    global person_found
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    media_ctrl.play_sound(rm_define.media_sound_attacked)
    person_found = True

def scan_for_person_and_play_sound():
    global person_found
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    person_found = false
    while person_found = false
        gimbal_ctrl.rotate_with_degree(rm_define.clockwise, -250)
        gimbal_ctrl.rotate_with_degree(rm_define.clockwise, 250)





