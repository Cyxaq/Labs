#!/bin/bash

api="41234bb3434e46ab8431e8296035aca5"

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
