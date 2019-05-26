#!/bin/bash

if ! hash python; then
    echo "Python não instalado. É necessário possui a versao Python 2.7 ou superior."
    echo "Para instalar, execute o aplicativo SETUP.desktop e aguarde o término da instalação."
    echo "Para instalar será solicitada a sua senha da máquina"
fi

ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -lt "27" ]; then
    echo "This script requires python 2.7 or greater"
    exit 1
fi

DSUS_EXTRACTOR_ROOT_PATH=$(dirname $(dirname $0))

PYTHON_DSUS_PATH=DSUS_EXTRACTOR_ROOT_PATH/.ubuntu-python-src
PIP_LOCAL=$PYTHON_DSUS_PATH/bin/pip
PYTHON_LOCAL=$PYTHON_DSUS_PATH/bin/python

cd $DSUS_EXTRACTOR_ROOT_PATH/.src

$PIP_LOCAL install -r requirements.txt

cd $DSUS_EXTRACTOR_ROOT_PATH/.src/webserver/

echo ">>>>>>>>>>>>>>>>>>>>>>>>INICIANDO APLICACAO<<<<<<<<<<<<<<<<<<<<<<<<"

# executa o segundo sem esperar o primeiro terminar pra abrir a janela qdo o servidor já estiver ok
$PYTHON_LOCAL open_url.py & $PYTHON_LOCAL server.py


echo ">>>>>>>>>>>>>>>>>>>>>>>>Aplicação encerrada. Feche o terminal.<<<<<<<<<<<<<<<<<<<<<<<<"


ping localhost
