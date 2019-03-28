def encrypt(e,n,P):
	
	i=1
	itr = 2
	data = []
	data.append(P)
	while(itr <= e):
		data.append((data[i-1]**2) %n)
		i+=1
		itr= itr*2
	i=0
	C=1
	while(e>0):
		if e %2 ==1:
			C = (C* data[i]) %n
		e= e//2
		i+=1 
	return C 


def decrypt(d,n,C):
	i=1
	itr = 2
	data = []
	data.append(C)
	while(itr <= d):
		data.append((data[i-1]**2) %n)
		i+=1
		itr= itr*2
	i=0
	P=1
	while(d>0):
		if d %2 ==1:
			P = (P* data[i]) %n
		d= d//2
		i+=1 
	return P
