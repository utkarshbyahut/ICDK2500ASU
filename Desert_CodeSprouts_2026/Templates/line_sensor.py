# Demonstrates the IR sensors on the 3pi+ robot: the left and right
# bump sensors on the front of the robot and the five downward-looking
# reflectance/line sensors.
#
# Press A to calibrate both sets of sensors.
#
# Press C to switch the line sensors to display calibrated or
# uncalibrated values.

from pololu_3pi_2040_robot import robot
import time

line_sensors = robot.LineSensors()
motors = robot.Motors()
display = robot.Display()

button_a = robot.ButtonA()

calibration_speed = 1000
calibration_count = 200

line_sensors.start_read()
time.sleep_ms(2)

display.text("Place on line", 0, 0)
display.text("and press A to", 0, 10)
display.text("calibrate.", 0, 20)
display.show()

while not button_a.check():
    pass

display.fill(0)
display.show()
time.sleep_ms(500)

motors.set_speeds(calibration_speed, -calibration_speed)
for i in range(calibration_count/4):
    line_sensors.calibrate()

motors.off()
time.sleep_ms(200)

motors.set_speeds(-calibration_speed, calibration_speed)
for i in range(calibration_count/2):
    line_sensors.calibrate()

motors.off()
time.sleep_ms(200)

motors.set_speeds(calibration_speed, -calibration_speed)
for i in range(calibration_count/4):
    line_sensors.calibrate()

motors.off()

while True:
    line = line_sensors.read_calibrated()

    # 64-40 = 24
    scale = 24/1023

    display.fill_rect(0, 40, 128, 24, 0)

    display.fill_rect(36, 64-int(line[0]*scale), 8, int(line[0]*scale), 1)
    display.fill_rect(48, 64-int(line[1]*scale), 8, int(line[1]*scale), 1)
    display.fill_rect(60, 64-int(line[2]*scale), 8, int(line[2]*scale), 1)
    display.fill_rect(72, 64-int(line[3]*scale), 8, int(line[3]*scale), 1)
    display.fill_rect(84, 64-int(line[4]*scale), 8, int(line[4]*scale), 1)

    display.show()
