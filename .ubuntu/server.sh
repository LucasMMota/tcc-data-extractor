#!/bin/bash

unset PYTHONPATH

DSUS_EXTRACTOR_ROOT_PATH=$(dirname $0)
#PIP_LOCAL=$DSUS_EXTRACTOR_ROOT_PATH/.venv/bin/pip
#PYTHON_LOCAL=$DSUS_EXTRACTOR_ROOT_PATH/.venv/bin/python

cd $DSUS_EXTRACTOR_ROOT_PATH/.src

pip install -r requirements.txt

cd $DSUS_EXTRACTOR_ROOT_PATH/.src/webserver/

echo ">>>>>>>>>>>>>>>>>>>>>>>>INICIANDO APLICACAO<<<<<<<<<<<<<<<<<<<<<<<<"

# executa o segundo sem esperar o primeiro terminar pra abrir a janela qdo o servidor já estiver ok
python open_url.py & python server.py


echo ">>>>>>>>>>>>>>>>>>>>>>>>Aplicação encerrada. Feche o terminal.<<<<<<<<<<<<<<<<<<<<<<<<"


ping localhost