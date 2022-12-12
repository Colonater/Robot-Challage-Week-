


def start():
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
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 270)

#move rebot into room


    chassis_ctrl.move_with_distance(0, 4.70)
    gimbal_ctrl.recenter()

    chassis_ctrl.move_with_distance(180, 4.70)
