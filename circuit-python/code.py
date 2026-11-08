
# automatic CTC sign in signs
# Duane Strong 11/08/2026

import board
import digitalio
import pwmio
import adafruit_dotstar as dotstar
import time

# dotstart RGB LED on board
dots = dotstar.DotStar(board.DOTSTAR_CLOCK, board.DOTSTAR_DATA, 1, brightness=0.2)

# red LED on board
red_led = digitalio.DigitalInOut(board.LED)
red_led.direction = digitalio.Direction.OUTPUT
red_led.value = True

# sign LEDs PWM
enter_sign = pwmio.PWMOut( board.D2, frequency=5000, duty_cycle=0)
exit_sign = pwmio.PWMOut( board.D4, frequency=5000, duty_cycle=0)

# PIR sensor inputs
enter_pir = digitalio.DigitalInOut(board.D0)
enter_pir.direction = digitalio.Direction.INPUT
exit_pir = digitalio.DigitalInOut(board.D1)
exit_pir.direction = digitalio.Direction.INPUT


def flash_sign( sign ):

	# ramp up and down 4 times
	for t in range(4):
		for i in range( 1000, 65536, 5000 ):
			sign.duty_cycle = i
			time.sleep(.05)
		for i in range( 65535, 0, -5000 ):
			sign.duty_cycle = i
			time.sleep(.05)
	# full brightness for 5 second
	sign.duty_cycle = 65535
	time.sleep(5)
	# off
	sign.duty_cycle = 0

while True:
	if enter_pir.value:
		dots[0] = (0,255,0)
		print("entering...")
		flash_sign( enter_sign )
		print("done")
		dots[0] = (0,0,0)
	if exit_pir.value:
		dots[0] = (255,0,0)
		print("exiting...")
		flash_sign( exit_sign )
		print("Done")
		dots[0] = (0,0,0)

		
