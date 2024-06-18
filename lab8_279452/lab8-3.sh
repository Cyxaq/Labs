#!/bin/bash

ip=$1

api="Y6mv2BbNAhaj6gZOX6fj6WWyNi8fFXzl"

url="https://api.shodan.io/shodan/host/$ip?key=$api"

res=$(curl -s "$url")

info=$(echo "$response" | jq -r '{
    "IP": .ip_str,
    "Organization": .org,
    "ISP": .isp,
    "Country": .country_name,
    "Region": .region_code,
    "City": .city
}')
ans=$(echo "$res" | jq -r '.ports[]')

echo "Podstawowe dane dla IP $ip:"
echo "$info"

# Wyświetlenie listy otwartych portów
echo "Otwartych portów dla IP $ip:"
echo "$ans"
