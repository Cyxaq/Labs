#!/bin/bash



help(){
	echo
	echo "Użycie: "
	echo
	echo "Po urochomieniu skryptu podaj slowo kluczowe "
	echo "(Np. targi)"
	echo
	echo "Skrypt wyszukuje artykuly z portalu informacyjnego (news api)"
}


if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]
then
	help
	exit 0
fi

api="41234bb3434e46ab8431e8296035aca5"

echo "Podaj slowo kluczowe: "
read temat

url="https://newsapi.org/v2/everything"

response=$(curl -s -G \
    --data-urlencode "q=$temat" \
    --data-urlencode "apiKey=$api" \
    "$url")

articles=$(echo "$response" | jq -r '.articles[] | "\(.title)\n\(.description)\n\(.url)\n"')

if [ -z "$articles" ]; then
    echo "Nie znaleziono artykułów! >:("
else
    
    echo "$articles"
fi
