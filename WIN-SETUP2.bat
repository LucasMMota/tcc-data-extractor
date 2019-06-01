@ECHO OFF

ECHO .
ECHO .
ECHO .
ECHO INICIANDO INSTALACAO DOS REQUISITOS, PODE DEMORAR ALGUNS MINUTOS
ECHO AGUARDE ATE MENSAGEM DE FINALIZACAO DA INSTALACAO
ECHO .
ECHO .
ECHO .

:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

pip --version 2>NUL
if errorlevel 1 goto errorNoPython

CD "C:\Program Files\R\R-3.6.0\bin\"
R.exe --version 2>NUL
if errorlevel 1 goto errorNoRscript
goto:setupStep
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


:setupStep
ECHO "Verificando dependencias do projeto. Aguarde por favor."
set DATASUS_WORKINGDIR=%~dp0
set DATASUS_WEBSERVERDIR=%~dp0.src\webserver\
::SET DSUS_PYPATH=%DATASUS_WORKINGDIR%win\Scripts\

pip install Flask
pip install pandas

:: retry
pip install Flask
pip install pandas

CD "C:\Program Files\R\R-3.6.0\bin\"
Rscript.exe %DATASUS_WORKINGDIR%.src\r-requirements.r

ECHO .
ECHO .
ECHO .
ECHO ">>> INSTALACAO REALIZADA COM SUCESSO! FECHE O TERMINAL."

PAUSE