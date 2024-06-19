#!/bin/bash

help(){
	echo
	echo "Użycie: "
	echo
	echo "Po urochomieniu skryptu podaj nazwe waluty"
	echo '(Np. czk)'
	echo
	echo "Skrypt pokazuje kurs wporwadzonej waluty w ciągu ostatnich pięciu dni"
	echo
	echo "Oprocz tego pokazuje zmiane kursu (dodatnia liczba oznacza ze kurs wzrosl, ujemna - sie zmniejszyl)"
}


if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]
then
	help
	exit 0
fi



echo "Podaj nazwe waluty wg standartu ISO 4217 (np. pln)"
read name

echo $data


url="http://api.nbp.pl/api/exchangerates/rates/a/$name/last/5/?format=json" 

json=$(curl $url)

if [[ "$json" == *"Brak danych"* ]]
then
	echo "brak danych"
	exit
fi

if [[ "$json" == *"404"* ]]
then
	echo "blad"
	exit
fi

mids=($(echo "$json" | jq -r '.rates[].mid'))

k=0

echo "kursy waluty ($name) w ciagu pieciu ostatnich dni"
echo ${mids[@]}

k=${#mids[@]}

i=1

q=${mids[0]}

echo

echo "zmiany kursu: "
while [ $i -lt 5 ]
do
	w=${mids[$i]}
	ans=$(awk "BEGIN {print $w - $q}")
	echo $ans
	q=${mids[$i]}
	
	
	let i=$i+1
done
