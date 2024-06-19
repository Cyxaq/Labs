from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

ivec = get_random_bytes(8)
key = get_random_bytes(8)

cipher = DES.new(key, DES.MODE_CBC, ivec)

path = str(input("Wprowadź ścieżkę do plika: "))
arr_fold = path.split('/')
filename = arr_fold[-1]

with open(path, 'rb') as file:
    txt = file.read()

paddedTxt = pad(txt, DES.block_size)

cipherTxt = cipher.encrypt(paddedTxt)

encr_filename = filename.replace('.txt', '.enc')
with open("files/encrypted/"+encr_filename, 'wb')as file:
    file.write(ivec+cipherTxt)

key_filename = filename.replace('.txt', '.key')

keys_info = f"Initialization vector:{ivec} \nKey:{key}"
with open("files/keys/"+key_filename, 'w') as file:
    file.write(keys_info)
