import subprocess
from .constants import SRC_DIR, RAW_FILES_DIR, CONVERTED_FILES_DIR


def dbc2csv(raw_filename):
    dbc2csv_path = SRC_DIR + "/dbc2csv.R " + RAW_FILES_DIR + " " + CONVERTED_FILES_DIR + " " + raw_filename

    tries = 2
    while tries > 0:
        try:
            print(subprocess.call("/usr/local/bin/Rscript --vanilla " + dbc2csv_path, shell=True))
            tries = 0
            return True
        except:
            print("(R) Erro ao converter o arquivo: " + raw_filename)
            tries -= 1

    return False

