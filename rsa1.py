from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import pickle


def newkeys(keysize):
    random_gen = Random.new().read
    key = RSA.generate(keysize,random_gen)
    priv,pub = key.exportKey('PEM'),key.publickey().exportKey('PEM')
    return priv,pub


def encrypt(pub_key,message):
    cipher = PKCS1_OAEP.new(RSA.importKey(pub_key))
    return cipher.encrypt(message)

def decrypt(priv_key,ciphertext):
    cipher = PKCS1_OAEP.new(RSA.import_key(priv_key))
    return cipher.decrypt(ciphertext)



with open('keys.pkl','rb') as f:
    x = pickle.load(f)

with open('pickle_file_name.pkl','rb') as f:
    y = pickle.load(f)

#newkeys(8192)
#pickle.dump(newkeys(8192), open('pickle_file_name.pkl', 'wb'))
privateserv, publicserv, privatea,publica,privateb,publicb = x
privateserv, publicserv = y

