import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)



# Relay mati (kalau true)
# GPIO.output(16, True)
# GPIO.output(20, True)
# GPIO.output(21, True)

# Relay hidup (kalau aktif false)
GPIO.output(16, False)
# GPIO.output(20, False)
# GPIO.output(21, False)



# Jika USB terhubung ke PC yang menyala, maka relay tetap hidup
# Jika USB TIDAK terhubung ke PC / PC mati, maka relay mati

# if GPIO.input(16):			# relay true / mati
# 	print "relay mati"
# if not GPIO.input(16):		# relay false / hidup
# 	print "relay hidup"

# if not GPIO.input(16) or not GPIO.input(21) :
while True:
	inputPC_1 = GPIO.input(13)
	inputPC_2 = GPIO.input(19)

	if (inputPC_1 == True):
		time.sleep(1)
		print('USB 1 Terhubung')
		# GPIO.output(16, False)
	else:
		print('USB 1 Tidak terhubung')
		relayON = True
		time.sleep(5)
		if(relayON):
			print("masih belum hidup")
			GPIO.output(16, True)

	inputPC_3 = GPIO.input(26)
	if (inputPC_3 == True):
		time.sleep(1)
		print('USB 3 Terhubung')
		# GPIO.output(16, False)
	else:
		print('USB 3 Tidak terhubung')
		relayON = True
		time.sleep(5)
		if(relayON):
			print("masih belum hidup")
			GPIO.output(21, True)


