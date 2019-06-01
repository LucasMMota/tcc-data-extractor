### DataSUS downloader
This project aims to access a given DataSUS system databse and download its data into a local or remote repository (on a Data Staging).

Example:
 
`python datasus_loader.py --system=SIASUS --dateFrom=01/2010 --dateTo=12/2011 --states=SP,RJ `
###Steps

#####Extraction

* connect to FTP (whether necessary do it before)
* Download file into `raw-files`

#####Transform
* Convert (through R script) and save into `converted-files`
* Deletes source (`.dbc`)

#####Load
* Save into a chosen Data Staging Database (decide which?)



#####Questions:
* Needs filters (data) to download the files
* which DB use?
    - needs research and references (maybe casandra)
* which transformation would it be necessary (like data quality)?
    - Victor can handle this
* It will be a hardcoded system on script, it should make it possible to chose wich Datasus system to access.


#####Todos
* apresentar no trabalho todo o layout dos arquivos do datasus
    - pedir pro victor fazer isso
* e explicar como funciona




WIN
    .src
    Python-Instalador.exe
    Setup.bat
    Aplicacao.bat

Ubuntu
    .src
    Setup.sh
    Aplicacao.sh

Mac
    .src
    Setup.sh
    Aplicacao.sh


// WIN
    solicitar que instale python ou ver se funciona colocar a pasta junto
    win-server inicia server e abre aplicacao

//ubuntu
    É recomendável possuir antes o Python, PIP e R instalados. No entanto caso não possua é possível instalar
    através do arquivo `setup.sh`

    setup instala Python, PIP e R

    Basta acessa a aplicacao abrindo o arquivo Aplicacao.sh que ira iniciar a aplicacao via web browser e ficará rodando em background


//mac
    igual ubuntu
    
    depois conectar com um bd...
            essa parte vai ser tudo manual o cara so poe os detalhes de conexao
    Verificar textos
    Fazer documentacao de tudo / isntrucoes para usuario

# todo fazer bench de qto tempo gasta com ferramentas diferentes
                # ver tempo que gasta pra instalar qdo for colocar nas isntrucoes

