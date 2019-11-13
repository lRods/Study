from Crypto.Cipher import DES
key = b'-8B key-'
cipher = DES.new(key, DES.MODE_OFB)
text = input("Digite um texto para encriptar: ")
plaintext = text.encode('utf-8')
msg = cipher.iv + cipher.encrypt(plaintext)
print(msg)


cipher = DES.new(key, DES.MODE_OFB)
msg = cipher.iv + cipher.decrypt(msg)
print(msg)