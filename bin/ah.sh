#!/usr/bin/bash

if [ ! -e ../config/accounts_path.txt ]; then
	touch ../config/accounts_path.txt
fi

ACCOUNTS_PATH=$(cat ../config/accounts_path.txt)
cd scripts

if [ "$ACCOUNTS_PATH" == "" ]; then
	./configure.sh
	exit
fi

echo "Choissisez le mode que vous souhaitez : "
read op

if [ "$op" == "m" -o "$op" == "modif" -o "$op" == "modifier" ]; then
	./modify.sh
fi

if [ "$op" == "n" -o "$op" == "nouv" -o "$op" == "nouveau" ]; then
	./new.sh
fi

if [ "$op" == "r" -o "$op" == "refresh" ]; then
	./refresh.sh
fi

if [ "$op" == "v" -o "$op" == "version" ]; then
	./version.sh
fi

read end