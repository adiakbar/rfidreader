
from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 3030, LoggingNamespace) as socketIO:
    status = {
    	'mahasiswa': 'M. Adi Akbar',
        'rfid': '1',
        'tanggal': '2015-10-12',
        'ruangan': 'Laboratorium A',
    	'kd_ruangan': 0,
        'komputer': 'Komputer 1',
    	'kd_komputer': 0,
    	'kondisi': 'on'
    }
    socketIO.emit('status_added', status)
    socketIO.wait(seconds=1)


# VIRTUAL_ENV=$HOME/.virtualenv
# source $VIRTUAL_ENV/bin/activate
