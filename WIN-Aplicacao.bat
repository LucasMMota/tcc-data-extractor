@ECHO OFF

:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

pip --version 2>NUL
if errorlevel 1 goto errorNoPython

CD "C:\Program Files\R\R-3.6.0\bin\"
R.exe --version 2>NUL
if errorlevel 1 goto errorNoRscript
goto:initAplication
goto:eof

:errorNoRscript
ECHO ========================ALERTA========================================
ECHO O script R nao esta instalado nesse computador, por favor instale-o atraves
ECHO do instalador R-XTPO que pode ser encontrado nesse diretorio (em caso de duvidas veja o arquivo "AJUDA.txt"
ECHO ======================================================================

PAUSE

:errorNoPython
ECHO ========================ALERTA========================================
ECHO PYTHON nao esta instalado nesse computador, por favor instale-o atraves
ECHO do instalador XTPO que pode ser encontrado nesse diretorio
ECHO Lembre-se de instalar o PIP (em caso de duvidas veja o arquivo "AJUDA.txt"
ECHO ======================================================================

PAUSE

:initAplication
ECHO .
ECHO .
ECHO .
ECHO ">>>>>>>>>>>>>>>>>>>>>>>>INICIANDO APLICACAO<<<<<<<<<<<<<<<<<<<<<<<<"
ECHO .
ECHO .
ECHO .

set DATASUS_WORKINGDIR=%~dp0
set DATASUS_WEBSERVERDIR=%~dp0.src\webserver

CD %DATASUS_WEBSERVERDIR%
python open_url.py & python server.py

ECHO ">>>>>>>>>>>>>>>>>>>>>>>>Aplicacao encerrada. Feche o terminal.<<<<<<<<<<<<<<<<<<<<<<<<"

PAUSE