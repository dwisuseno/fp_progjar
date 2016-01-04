import socket
import select
import sys
import os
import pickle
import random

host = 'localhost'
print "port:"
port = input()
alamat = (host,port)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind(alamat)
server.listen(5)
input_socket = [server]


deck = list()
pegangan = list()
pegangan2 = list()


# Mulai Kartu
class Card:
    def __init__(self, faceNum, suitNum):
        self.faceNum = faceNum
        self.suitNum = suitNum

    def getCardName(self):
          nameSuit = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
          nameFace = ['Wajik','Waru','Semanggi','Hati']
          return "%s %s %s" % (self.suitNum,  nameSuit[self.suitNum], nameFace[self.faceNum])

    def __str__(self):
        carte_print1 = str(self.faceNum)
        carte_print2 = str(self.suitNum)
        return carte_print1 +('-')+ carte_print2

class Player:
    def __init__(self,ID,Card):
        #self.PlayerID = ID
        #print Card
        self.PlayerID = ID
        self.deck = Card # this will hold a list of Card objects
    def flag(self):
        return self.PlayerID, self.deck


def deck():
    deck = []
    for suitNum in range(13):
        for faceNum in range(4):
            deck.append(Card(faceNum, suitNum))
    return deck

deck = deck()
for card in range(0,5):
    pegangan.append(deck[card].getCardName())
    random.shuffle(deck)
    pegangan2.append(deck[card].getCardName())

player1 = Player(1, pegangan)
player2 = Player(2, pegangan2)
#print Player.flag(player1)
#print Player.flag(player2)

def bandingKartu(x,y):
    if x > y:
        return x
    elif x == y:
        return "podo"
    else:
        return y
# akhir kartu

# Kelas Server
class Server:
    def __init__(self,IP,PORT):
        self.IP = IP
        self.PORT = PORT


try:
    while True:
        read_ready,write_ready, exception = select.select(input_socket, [], [])
        for sock in read_ready:
            if sock == server:
                client_socket, client_address = server.accept()
                input_socket.append(client_socket)
                                   
                print "sudah tersambung dari client :", client_address

            else:
                test = sock.recv(1024)
                print test
                #print Player.flag(player1)
                #header = 7389
                p = pickle.dumps(Player.flag(player1))
                sock.send(p)
except KeyboardInterrupt:
    input_socket.remove(server)
    server.close()
    sys.exit(0)
