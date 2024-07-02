from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()



filenameToSign = str(input("Wprowadź nazwę plika do podpisania: "))

with open("files/keys/Public/"+(filenameToSign.replace('.txt', '.key')), 'w') as file:
    file.write(str(public_key.export_key()))

with open("files/keys/Private/"+(filenameToSign.replace('.txt', '.key')), 'w') as file:
    file.write(str(private_key.export_key()))


with open("files/UnSigned/"+filenameToSign, 'rb') as file:
    txt = file.read()
hash = SHA256.new(txt)
sign = pkcs1_15.new(private_key).sign(hash)

signedFilename = filenameToSign+'.sig'
with open("files/Signed/"+signedFilename, 'bw') as file:
    file.write(sign)
