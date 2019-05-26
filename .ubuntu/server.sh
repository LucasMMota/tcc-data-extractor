#!/bin/bash

unset PYTHONPATH

DSUS_EXTRACTOR_ROOT_PATH=$(dirname $(dirname $0))
PIP_LOCAL=$DSUS_EXTRACTOR_ROOT_PATH/ubuntu-python-src/bin/pip3
PYTHON_LOCAL=$DSUS_EXTRACTOR_ROOT_PATH/ubuntu-python-src/bin/python3

cd $DSUS_EXTRACTOR_ROOT_PATH/.src

$PIP_LOCAL install -r requirements.txt

cd $DSUS_EXTRACTOR_ROOT_PATH/.src/webserver/

echo ">>>>>>>>>>>>>>>>>>>>>>>>INICIANDO APLICACAO<<<<<<<<<<<<<<<<<<<<<<<<"

# executa o segundo sem esperar o primeiro terminar pra abrir a janela qdo o servidor já estiver ok
$PYTHON_LOCAL open_url.py & $PYTHON_LOCAL server.py


echo ">>>>>>>>>>>>>>>>>>>>>>>>Aplicação encerrada. Feche o terminal.<<<<<<<<<<<<<<<<<<<<<<<<"


ping localhost
