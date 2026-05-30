from pololu_3pi_2040_robot import robot
import time

#display = robot.Display()
motors = robot.Motors()
#line_sensors = robot.LineSensors()

button_a = robot.ButtonA()


def motor_speed(left_speed, right_speed):
    if left_speed > 2000:
        left_speed = 2000
    
    if left_speed < -2000:
        left_speed = -2000

    if right_speed > 2000:
        right_speed = 2000

    if right_speed < -2000:
        right_speed = -2000
    
    motors.set_speeds(left_speed, right_speed)

    return 0


def get_track_position(line, threshold):
    if line[2] > threshold:
        return "center"
    elif line[0] > threshold or line[1] > threshold:
        return "left"
    elif line[3] > threshold or line[4] > threshold:
        return "right"
    else:
        return "lost"



def calibrate(line_sensors, display):

    calibration_speed = 1000
    calibration_count = 400
    calibration_time = 200

    display.text("Place on line", 0, 0)
    display.text("and press A to", 0, 10)
    display.text("calibrate.", 0, 20)
    display.show()

    while not button_a.check():
        pass

    display.fill(0)
    display.show()
    time.sleep_ms(calibration_time)

    motors.set_speeds(calibration_speed, -calibration_speed)
    for i in range(calibration_count/4):
        line_sensors.calibrate()

    motors.off()
    time.sleep_ms(calibration_time)

    motors.set_speeds(-calibration_speed, calibration_speed)
    for i in range(calibration_count/2):
        line_sensors.calibrate()

    motors.off()
    time.sleep_ms(calibration_time)

    motors.set_speeds(calibration_speed, -calibration_speed)
    for i in range(calibration_count/4):
        line_sensors.calibrate()

    motors.off()

def draw_histogram(line, display):
    # 64-40 = 24
    scale = 24/1023

    display.fill_rect(36, 64-int(line[0]*scale), 8, int(line[0]*scale), 1)
    display.fill_rect(48, 64-int(line[1]*scale), 8, int(line[1]*scale), 1)
    display.fill_rect(60, 64-int(line[2]*scale), 8, int(line[2]*scale), 1)
    display.fill_rect(72, 64-int(line[3]*scale), 8, int(line[3]*scale), 1)
    display.fill_rect(84, 64-int(line[4]*scale), 8, int(line[4]*scale), 1)
    display.show()
