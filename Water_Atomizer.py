import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
r_pwm_pin = 13  # RPWM
l_pwm_pin = 6   # LPWM
r_en_pin = 26   # R_EN
l_en_pin = 16   # L_EN

# Set up GPIO pins as outputs
GPIO.setup(r_pwm_pin, GPIO.OUT)
GPIO.setup(l_pwm_pin, GPIO.OUT)
GPIO.setup(r_en_pin, GPIO.OUT)
GPIO.setup(l_en_pin, GPIO.OUT)

# Function to set motor speed
def set_motor_speed(pwm_pin, speed):
    pwm = GPIO.PWM(pwm_pin, 1000)  # Create PWM object with frequency 1000Hz
    pwm.start(0)  # Start PWM with duty cycle 0
    pwm.ChangeDutyCycle(speed)  # Set duty cycle (0-100) to control speed

# Function to enable motor
def enable_motor(en_pin):
    GPIO.output(en_pin, GPIO.HIGH)  # Set EN pin high to enable motor

# Function to disable motor
def disable_motor(en_pin):
    GPIO.output(en_pin, GPIO.LOW)  # Set EN pin low to disable motor

try:
    # Main loop
    while True:
        enable_motor(r_en_pin)  # Enable right motor
        enable_motor(l_en_pin)  # Enable left motor
        set_motor_speed(r_pwm_pin, 50)  # Set right motor speed to 50% (example)
        set_motor_speed(l_pwm_pin, 50)  # Set left motor speed to 50% (example)
        time.sleep(5)  # Run motors for 5 seconds
        disable_motor(r_en_pin)  # Disable right motor
        disable_motor(l_en_pin)  # Disable left motor
        time.sleep(10)  # Pause for 10 seconds

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()
