import RPi.GPIO as GPIO
import time

# Define pins
LPWM = 25
RPWM = 24
L_EN = 22
R_EN = 23

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(L_EN, GPIO.OUT)
GPIO.setup(R_EN, GPIO.OUT)

# Set initial motor direction and speed
GPIO.output(L_EN, GPIO.HIGH)  # Left motor enable
GPIO.output(R_EN, GPIO.HIGH)  # Right motor enable

# Function to set motor speed
def set_motor_speed(pwm_pin, speed):
    pwm = GPIO.PWM(pwm_pin, 1000)  # Create PWM object with frequency 1000 Hz
    pwm.start(0)  # Start PWM with duty cycle 0 (off)
    pwm.ChangeDutyCycle(speed)  # Set duty cycle (0-100) for speed control

try:
    while True:
        # Move forward
        GPIO.output(LPWM, GPIO.HIGH)
        GPIO.output(RPWM, GPIO.HIGH)
        set_motor_speed(LPWM, 50)  # Set left motor speed to 50%
        set_motor_speed(RPWM, 50)  # Set right motor speed to 50%
        time.sleep(2)  # Move forward for 2 seconds

        # Stop
        GPIO.output(LPWM, GPIO.LOW)
        GPIO.output(RPWM, GPIO.LOW)
        time.sleep(1)  # Pause for 1 second

        # Move backward
        GPIO.output(LPWM, GPIO.LOW)
        GPIO.output(RPWM, GPIO.LOW)
        set_motor_speed(LPWM, 50)  # Set left motor speed to 50%
        set_motor_speed(RPWM, 50)  # Set right motor speed to 50%
        time.sleep(2)  # Move backward for 2 seconds

        # Stop
        GPIO.output(LPWM, GPIO.LOW)
        GPIO.output(RPWM, GPIO.LOW)
        time.sleep(1)  # Pause for 1 second

except KeyboardInterrupt:
    GPIO.cleanup()  # Cleanup GPIO on Ctrl+C exit
