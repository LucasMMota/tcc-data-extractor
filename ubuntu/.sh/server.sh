#!/bin/bash

echo 'Abrindo.....'

DSUS_EXTRACTOR_ROOT_PATH=$(dirname $(dirname $(dirname $0)))

cd $DSUS_EXTRACTOR_ROOT_PATH/.src

pip install -r requirements.txt

cd $DSUS_EXTRACTOR_ROOT_PATH/.src/webserver/

python server.py
ping localhost