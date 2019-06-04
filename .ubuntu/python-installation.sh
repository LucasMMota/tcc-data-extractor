#!/bin/bash

if ! hash python; then
	sudo apt-get install python
fi

if ! hash pip; then
	sudo apt-get install python-pip
fi

if ! hash Rscript; then
	sudo apt-get install r-base
fi

DSUS_EXTRACTOR_ROOT_PATH=$(dirname $(dirname $0))
cd $DSUS_EXTRACTOR_ROOT_PATH/.src

pip install Flask
pip install pandas
pip install mysql.connector
if hash pg_config; then
    pip install psycopg2
fi

# retry
if hash pg_config; then
    pip install psycopg2
fi
pip install mysql.connector
pip install pandas
pip install Flask

Rscript r-requirements.r

echo " "
echo " "
echo " "
echo ">>> Instalação realizada com sucesso! Feche o terminal."
wait $!

while [ 1 ]
do
	echo ""
	sleep 100
done	