#!/bin/bash

if ! hash python; then
	echo " "
	echo " "
	echo " "
    echo "Python não instalado. É necessário possui a versao Python 2.7 ou superior."
    echo "Para instalar, execute o aplicativo SETUP.desktop e aguarde o término da instalação."
    echo "Para instalar será solicitada a sua senha da máquina."
    echo "Quando for perguntado se deseja continuar: 'DO you want to continue yn' Yn, insira Y e aguarde."		
    wait $!
    while [ 1 ]
    do
        echo ""
        sleep 100
    done
    exit 1
fi

ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -lt "27" ]; then
    echo "This script requires python 2.7 or greater"
    wait $!
    while [ 1 ]
    do
        echo ""
        sleep 100
    done
    exit 1
fi

DSUS_EXTRACTOR_ROOT_PATH=$(dirname $(dirname $0))
cd $DSUS_EXTRACTOR_ROOT_PATH/.src/webserver/

echo ">>>>>>>>>>>>>>>>>>>>>>>>INICIANDO APLICACAO<<<<<<<<<<<<<<<<<<<<<<<<"

# executa o segundo sem esperar o primeiro terminar pra abrir a janela qdo o servidor já estiver ok
python open_url.py & python server.py


echo ">>>>>>>>>>>>>>>>>>>>>>>>Aplicação encerrada. Feche o terminal.<<<<<<<<<<<<<<<<<<<<<<<<"


ping localhost
