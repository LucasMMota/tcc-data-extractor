import subprocess
import commands
from .constants import SRC_DIR, RAW_FILES_DIR, CONVERTED_FILES_DIR
import platform


def dbc2csv(raw_filename):
    dbc2csv_path = SRC_DIR + "/dbc2csv.R " + RAW_FILES_DIR + " " + CONVERTED_FILES_DIR + " " + raw_filename

    tries = 2
    while tries > 0:
        try:
            if platform.system().lower() == 'windows':
                dbc2csv_path = dbc2csv_path.replace('/', '\\')
                R_PATH = '\"C:\Program Files\R\R-3.6.0\\bin\\Rscript.exe\"'
                result = subprocess.call(R_PATH + " " + dbc2csv_path, shell=True)
                print(result)
                tries = 0
                return True
            else:
                R_PATH = commands.getstatusoutput('which Rscript')[1]
                result = subprocess.call(R_PATH + " --vanilla " + dbc2csv_path, shell=True)
                print(result)
                tries = 0
                return True
        except:
            print("(Rscript) Erro ao converter o arquivo: " + raw_filename)
            tries -= 1

    return False

