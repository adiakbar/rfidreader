# belum selesai sampai hidupkan relay dan mematikan relay
# kita pake server di hostinger (service) dan server di siskom (frontend)

import RPi.GPIO as GPIO
import MFRC522
import signal
import datetime
import requests

from Adafruit_CharLCD import Adafruit_CharLCD
from socketIO_client import SocketIO, LoggingNamespace


# DEKLARASI VARIABEL
namaHari = ["senin","selasa","rabu","kamis","jum\'at","sabtu","minggu"]
gpio = [21,20,16]
komputer = ['pc-3','pc-2','pc-1']
jmlPC = 3
ruangan = 'laboratorium-b'

# DEKLARASI WAKTU
waktu = datetime.datetime
jam = waktu.now().strftime("%H:%M:%S")
hari = waktu.today().weekday()
tanggal = waktu.today().strftime("%Y-%m-%d")

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio[0], GPIO.OUT)
GPIO.setup(gpio[1], GPIO.OUT)
GPIO.setup(gpio[2], GPIO.OUT)

token = '';

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

		#print "Card read UID: ",idRFID
		#lcd.clear()
		#lcd.message(idRFID)


		# KIRIM REQUEST PENJADWALAN
		urlJdwl = "http://192.168.137.1:3000/api/action/validate"
		parameterJdwl = {'jam': jam, 'tanggal': tanggal, 'hari': namaHari[hari], 'rfid': idRFID, 'ruangan': ruangan, 'jmlPC': jmlPC}
		requestJdwl = requests.get(urlJdwl,params=parameterJdwl)
		responseJdwl = requestJdwl.json()
		statusJdwl = responseJdwl['success']
		pesanJdwl = responseJdwl['message']


		# KIRIM REQUEST MONITORING
		urlMntr = "http://192.168.137.1:3000/api/action/cek-status-off"
		parameterMntr = {'rfid': idRFID, 'tanggal': tanggal}
		requestMntr = requests.get(urlMntr,params=parameterMntr)
		responseMntr = requestMntr.json()
		statusMntr = responseMntr['success']
		pesanMntr = responseMntr['message']

		if statusJdwl == True and statusMntr == True:
			print pesanJdwl

			mahasiswa = responseJdwl['data']['mahasiswa']

			jmlPC -= 1
			print gpio[jmlPC]
			print komputer[jmlPC]
			# GPIO.output(gpio[jmlPC], True)


		# 	# with SocketIO('localhost', 3030, LoggingNamespace) as SocketIO:
		# 	# 	data = {
		# 	# 		'mahasiswa': mahasiswa,
		# 	# 		'rfid': idRFID,
		# 	# 		'tanggal': tanggal,
		# 	# 		'ruangan': ruangan,
		# 	# 		'komputer':
		# 	# 	}

		elif statusJdwl == True and statusMntr == False:
			print pesanMntr
		elif statusJdwl == False and statusMntr == True:
			print pesanJdwl
		else:
			print "ada Error Lain"


