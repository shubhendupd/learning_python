#Sample

from cryptography.fernet import Fernet

#generate key

key = Fernet.generate_key() # base 64
cipher = Fernet(key)

#encrypt

token = cipher.encrypt(b"m - hi sam")
print(token)

#decrypt

decrypt = cipher.decrypt(token)
print("decrypt")