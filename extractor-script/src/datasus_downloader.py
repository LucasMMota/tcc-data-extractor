import os
import ftplib
from .constants import RAW_FILES_DIR, ERROR_LOG_FILES_DIR
from os.path import exists
from converter import dbc2csv
import utils as utils


def save_log_on_errors(result, filename):
    if not exists(ERROR_LOG_FILES_DIR):
        os.makedirs(ERROR_LOG_FILES_DIR)

    if '226' not in result:
        log_name = ERROR_LOG_FILES_DIR+'not-downloaded.txt'

        with open(log_name, "a") as error_log:
            error_log.write(filename+'\n')


def save_log_non_existent_file(filename):
    if not exists(ERROR_LOG_FILES_DIR):
        os.makedirs(ERROR_LOG_FILES_DIR)

    log_name = ERROR_LOG_FILES_DIR+'not-existent-files.txt'

    with open(log_name, "a") as error_log:
        error_log.write(filename+' does not exist\n')


def if_file_is_empty_delete_it(raw_file):
    if os.stat(raw_file).st_size == 0:
        os.remove(raw_file)


def download(file_path, filename):
    print('Arquivo: ' + filename)

    raw_file = RAW_FILES_DIR + '' + filename

    try:
        ftp = ftplib.FTP("ftp.datasus.gov.br")
        ftp.login()
        ftp.cwd(file_path)
        result = ftp.retrbinary("RETR " + filename, open(raw_file, 'wb').write)
        ftp.quit()

        save_log_on_errors(result, filename)
        # todo it's better to delete on local after download than list all the files in ftp and check before download?
        if_file_is_empty_delete_it(raw_file)
    except:
        save_log_non_existent_file(filename)
        return


def download_and_convert(system, date_range, file_types, states):
    print('Iniciando carga de dados...')

    utils.create_raw_files()
    utils.create_converted_files()

    for date in date_range:
        for file_type in file_types:
            for state in states:
                print('Data: ' + date)
                print('Tipo de arquivos: ' + file_type)
                print('UF: ' + state)

                path_file, filename = utils.build_file_path(system, file_type, date, state)

                # Downloads files into raw-files
                download(path_file, filename)

                # Converts files and sabe on converted-files
                dbc2csv(filename)

    utils.clean_raw_files()


# Todo load into db
def load_to_database():
    return
