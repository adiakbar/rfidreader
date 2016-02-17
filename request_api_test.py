import requests
import datetime

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

# KIRIM REQUEST PENJADWALAN
urlJdwl = "http://localhost:3000/api/praktikum/prodi/1"
request = requests.get(urlJdwl)
response = request.json()

print response
