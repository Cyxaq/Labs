#!/bin/bash

echo "Pred podlaczeniem wprowadzic nastepujace komendy na uzadzeniu do ktorego sie podlaczamy:"
echo "sudo apt-get update && sudo apt-get install openssh-server"
echo "sudo systemctl start ssh"
echo

echo "Wprowadz nazwe uzytkownika"
read name


echo "Wprowadz ip gdzie sie podlaczasz:"
read ip

echo "Aby sie rozlaczyc wpisz \"exit\""


ssh $name@$ip




