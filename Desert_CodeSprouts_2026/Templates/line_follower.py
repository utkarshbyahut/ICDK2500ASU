from pololu_3pi_2040_robot import robot
from robot_functions import calibrate
from robot_functions import draw_histogram
from robot_functions import motor_speed
from robot_functions import get_track_position
import time

display = robot.Display()
line_sensors = robot.LineSensors()
button_a = robot.ButtonA()

# ----------------------------
# Line Follower
# ----------------------------

def follow_line(speed, threshold):
    last_direction = "center"

    display.fill(0)
    display.text("Tracking...", 0, 0)
    display.show()

    left_speed = speed
    right_speed = speed

    while True:
        line = line_sensors.read_calibrated()[:]
        line_sensors.start_read()

        position = get_track_position(line, threshold)

        display.fill(0)
        display.text("Track: " + position, 0, 10)
        display.show()

        # (5) Pass the correct values to each function to maneuver the robot. 
        if position == "center":
            # Call the function to set the motor speed to go straight.
            ret = motor_speed(left_speed, right_speed)
            last_direction = "center"

        elif position == "left":
            # Call the function to set the motor speed to turn left.
            ret = motor_speed(left_speed, right_speed)
            last_direction = "left"

        elif position == "right":
            # Call the function to set the motor speed to turn right.
            ret = motor_speed(left_speed, right_speed)
            last_direction = "right"

        else:  # Robot is lost
            if last_direction == "left":
                ret = motor_speed(500, 1000)
            elif last_direction == "right":
                ret = motor_speed(1000, 500)
            else:
                ret = motor_speed(0, 0)

        if ret < 0:
            display.fill(0)
            display.text("Error with speed!", 0, 0)
            display.show()

        draw_histogram(line, display)
        time.sleep_ms(10)


# ----------------------------
# Setup
# ----------------------------

# (1) Call the function to read line_sensors. 
#line_sensors.start_read()

time.sleep_ms(2)

# (2) Call the calibrate function to make the robot understand about the dark line and the surface.
#calibrate(line_sensors, display)

display.fill(0)
display.text("Press A to start", 0, 0)
display.show()

while not button_a.check():
    pass

# (3) Change the threshold value to detect the line better.
threshold = 1000

# (4) Change the speed of motors. Start with 900 as the speed value.
speed = 0

follow_line(speed, threshold)
