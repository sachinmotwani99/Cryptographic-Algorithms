from cryptography.fernet import Fernet

n = input("Enter the text you wish to encrypt using AES: ")
message = n.encode()

key = Fernet.generate_key()
f = Fernet(key)

print("The random key generated is : ",f)
encrypted = f.encrypt(message)

print("The final encrypted test is: ",encrypted)