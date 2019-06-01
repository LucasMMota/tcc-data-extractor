import subprocess
import commands
from .constants import SRC_DIR, RAW_FILES_DIR, CONVERTED_FILES_DIR
import platform


def dbc2csv(raw_filename):
    dbc2csv_path = SRC_DIR + "/dbc2csv.R " + RAW_FILES_DIR + " " + CONVERTED_FILES_DIR + " " + raw_filename

    tries = 2
    while tries > 0:
        try:
            if(platform.system() == 'Windows'):
                R_PATH = '\"C:\Program Files\R\R-3.6.0\\bin\\R.exe\"'
                print(">>>>>>>>>" + R_PATH + " --no-save < " + dbc2csv_path)  # todo remover

                result = subprocess.call(R_PATH + " --no-save < " + dbc2csv_path, shell=True)
                print(result)
                tries = 0
                return True
            else:
                R_PATH = commands.getstatusoutput('which Rscript')[1]
                # todo instalar pacote do R se nao estiver disponivel..
                # fazer bench de qto tempo gasta com ferramentas diferentes
                # ver tempo que gasta pra instalar qdo for colocar nas isntrucoes
                print("Rscript path: " + R_PATH) # todo remover
                print(">>>>>>>>>"+R_PATH + " --vanilla " + dbc2csv_path) # todo remover

                result = subprocess.call(R_PATH + " --vanilla " + dbc2csv_path, shell=True)
                print(result)
                tries = 0
                return True
        except:
            print("(R) Erro ao converter o arquivo: " + raw_filename)
            tries -= 1

    return False

