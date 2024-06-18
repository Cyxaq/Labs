#!/bin/bash


echo "Podaj nazwe waluty wg standartu ISO 4217 (np. pln)"
read name

echo $data


url="http://api.nbp.pl/api/exchangerates/rates/b/$name/last/5/?format=json" 

json=$(curl $url)

mids=($(echo "$json" | jq -r '.rates[].mid'))

k=0

clear

echo ${mids[@]}

k=${#mids[@]}

i=1

q=${mids[0]}


while [ $i -lt 5 ]
do
	w=${mids[$i]}
	#let roz=$w-$q | bc
	ans=$(awk "BEGIN {print $w - $q}")
	echo $ans
	q=${mids[$i]}
	
	
	let i=$i+1
done
