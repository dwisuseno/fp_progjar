import socket
import sys
import pickle

host = 'localhost'
print "port:"
port = input()
alamat = (host,port)
BUFFSIZE = 1024
hasil = list() 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(alamat)

def pilihan():
    if hasil:
        for item in hasil[1]:
            print item
        
    else:
        print "Selamat Datang Game Kartu"

try:
    while True:
        pilihan()
        respons = str(input())
        if respons == '1' or respons == '2':
            client.send(respons)
        elif respons == '3':
            break
        else:
            pilihan()
        m_header = client.recv(BUFFSIZE)
        hasil = pickle.loads(m_header)
        

except KeyboardInterrupt:
    print "Good bye"
    client.close()
    sys.exit(0)
