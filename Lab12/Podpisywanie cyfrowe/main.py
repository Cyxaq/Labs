from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()
# print(key)
# print(private_key)
# print(public_key)

