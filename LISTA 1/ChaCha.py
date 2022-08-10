import json
from base64 import b64encode
from CryptoCore.Cipher import ChaCha20
from CryptoCore.Random import get_random_bytes

plaintext = b'\0'*128
key = b'Kamil'+b'\0'*27

cipher = ChaCha20.new(key=key, nonce=b'00000000')
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

cipher = ChaCha20.new(key=key, nonce=b'00000000')
print(cipher.decrypt(ciphertext))

newFile = open("result", "wb")
newFileByteArray = bytearray(ciphertext)
newFile.write(newFileByteArray)
