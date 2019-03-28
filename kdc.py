import socket
from rsa1 import *
port = 12346
pr_Auth = [2,3]
# public_keys = [[7,123],[9,123]]
#privateKeyKdc,publicKeyA,PUblicKeyB= publicserv,privatea,privateb
privateKeyKdc,publicKeyA,PUblicKeyB = publicserv,publica,publicb

s = socket.socket()
s.bind(('',port))
s.listen(3)
while True:
	client,address = s.accept()
	requestforKey = client.recv(2048)
	request = requestforKey
	clientId = int(request.split(b';')[0])
	print(clientId)
	if clientId == 1:
		Key = str(publicKeyA) + ";" + str(request)
	else:
		Key = str(PUblicKeyB) + ";" + str(request)

	Key = encrypt(privateKeyKdc,Key.encode('utf-8'))
	client.send(Key)
s.close()