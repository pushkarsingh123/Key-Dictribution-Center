import socket 
import select 
import sys
from rsa1 import *
import uuid
import time
import threading

port_kdc = 12346
port_chatserver = 12345

publicKeyKdc,privateKeyA = privateserv,publica
#publicKeyKdc,privateKeyA = privateserv,publica
host = socket.gethostname()

def getpublickkeyForclient2():
	server_kdc = socket.socket() 
	host = socket.gethostname()       
	server_kdc.connect((host, port_kdc))

	nonce = str(uuid.uuid4().hex)
	request = "2;"+ str(time.time())+";"+ nonce
	#request = decrypt(publicKeyKdc,request.encode('utf-8'))

	server_kdc.send(request.encode('utf-8'))

	key = str(decrypt(publicKeyKdc,server_kdc.recv(2048)))
	publicKeyB = key[:key.index(";")]

	return publicKeyB
 

def receiveMessage(peer):
	while True:
		message = peer.recv(1024)
		if message:
			# decrypt call
			message = decrypt(privatea,message)
			message = "<Receiving message from  A>" + str(message)
			print(message)


def sendMessage(peer):
	message = input(": ")
	# encrypt call
	message = encrypt(publicb,message.encode('utf-8'))
	peer.send(message)


def listen(s):
	s.bind(('',port_chatserver))
	s.listen(5)
	peer, _ = s.accept()
	t1 = threading.Thread(target=receiveMessage, args=[peer])
	t1.start()
	t2 = threading.Thread(target=sendMessage, args=[peer])
	t2.start()


def connect(peer):         
	peer.connect((socket.gethostname(), port_chatserver))
	t1 = threading.Thread(target=receiveMessage, args=[peer])
	t1.start()
	t2 = threading.Thread(target=sendMessage, args=[peer])
	t2.start()

publicKeyB = getpublickkeyForclient2()
s = socket.socket()
listen(s)