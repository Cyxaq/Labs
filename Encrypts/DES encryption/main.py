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

"""
project zawiera folder "files" w którym:
    folder "plaintext" sluży dla przechowywania plików z tekstem niezaszyfrowanym
    folder "encrypted" - przechowywanie tych samych plików zaszyfrowanych
    folder "keys" - do szyfrowania wykorzystane podany klucz i IV
    
    Np. "plaintext/test1.txt" się zaszyfruje za pomocą IV i key z plika "keys/test1.key". Wynik będzie w "encrypted/test1.enc"
    
    za każdym razem jak szfrujemy dane klucz sie generuje ramdomowo (może cały czas się zmieniać)
"""
