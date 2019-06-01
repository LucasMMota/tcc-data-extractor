@ECHO OFF

set DATASUS_WORKINGDIR=%~dp0
set DATASUS_WEBSERVERDIR=%~dp0.src\webserver
@SET DSUS_PYPATH=%DATASUS_WORKINGDIR%\win\

CD %DATASUS_WEBSERVERDIR%
@CD %SUS_PYPATH%

ECHO ">>>>>>>>>>>>>>>>>>>>>>>>INICIANDO APLICACAO<<<<<<<<<<<<<<<<<<<<<<<<"

@ executa o segundo sem esperar o primeiro terminar pra abrir a janela qdo o servidor já estiver ok
python open_url.py & python server.py

ECHO ">>>>>>>>>>>>>>>>>>>>>>>>Aplicação encerrada. Feche o terminal.<<<<<<<<<<<<<<<<<<<<<<<<"

PAUSE