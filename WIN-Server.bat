#DSUS_EXTRACTOR_ROOT_PATH=$(dirname $(dirname %~dp0))
#cd $DSUS_EXTRACTOR_ROOT_PATH/.src/webserver/

set current_dir=%~dp0
echo %current_dir%

ECHO ">>>>>>>>>>>>>>>>>>>>>>>>INICIANDO APLICACAO<<<<<<<<<<<<<<<<<<<<<<<<"

# executa o segundo sem esperar o primeiro terminar pra abrir a janela qdo o servidor já estiver ok
python open_url.py & python server.py


ECHO ">>>>>>>>>>>>>>>>>>>>>>>>Aplicação encerrada. Feche o terminal.<<<<<<<<<<<<<<<<<<<<<<<<"

PAUSE