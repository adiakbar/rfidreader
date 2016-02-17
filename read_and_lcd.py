import RPi.GPIO as GPIO
import MFRC522
import signal
import datetime


from Adafruit_CharLCD import Adafruit_CharLCD

next_scan = True

def end_scan(signal,frame):
	global next_scan
	print "selesai"
	next_scan = False
	GPIO.cleanup()

signal.signal(signal.SIGINT, end_scan)

MIFAREReader = MFRC522.MFRC522()
lcd = Adafruit_CharLCD()

while next_scan:

	(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
	if status == MIFAREReader.MI_OK:
		print "Terdeteksi"

	(status,uid) = MIFAREReader.MFRC522_Anticoll()
	if status == MIFAREReader.MI_OK:
		idRFID = str(uid[0])+""+str(uid[1])+""+str(uid[2])+""+str(uid[3])
		
		print "Card read UID: ",idRFID
		lcd.clear()
		lcd.message(idRFID)
		

		


