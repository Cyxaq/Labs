#!/bin/bash


help(){
	echo
	echo "Użycie: "
	echo
	echo "Po urochomieniu skryptu podaj adres IP ktory chcesz zbadac "
	echo "(Np. 1.1.1.1)"
	echo
	echo "Skrypt wyszukuje: "
	echo "Organizacje tego IP"
	echo "ISP"
	echo "Panstwo w ktorym podany adres sie znajduje"
	echo "Region"
	echo "Miasto"
	echo
	echo "Oprocz tego pokazuje liste otwartych portow"
}


if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]
then
	help
	exit 0
fi



echo "Podaj adres IP: "
read ip

api="Y6mv2BbNAhaj6gZOX6fj6WWyNi8fFXzl"

url="https://api.shodan.io/shodan/host/$ip?key=$api"

res=$(curl -s "$url")

info=$(echo "$res" | jq -r '{
    "IP": .ip_str,
    "Organizacja": .org,
    "ISP": .isp,
    "Panstwo": .country_name,
    "Region": .region_code,
    "Miasto": .city
}')
ans=$(echo "$res" | jq -r '.ports[]')

echo "Podstawowe dane dla IP $ip:"
echo "$info"

# Wyświetlenie listy otwartych portów
echo "Otwarte porty dla IP $ip:"
echo "$ans"
