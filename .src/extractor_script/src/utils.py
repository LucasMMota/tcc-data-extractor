import os
import shutil
from constants import RAW_FILES_DIR, CONVERTED_FILES_DIR, DATASUS_SYSTEM_PATHS
import datetime
import pandas as pd


def build_file_path(system, file_type, date, state):
    path = DATASUS_SYSTEM_PATHS[system]
    filename = file_type + state + date + '.dbc'

    return path, filename


# Gets range data to read available files
def get_date_range(from_filter, to_filter):
    try:
        from_month = from_filter.split('/')[0]
        from_year = from_filter.split('/')[1]

        to_month = to_filter.split('/')[0]
        to_year = to_filter.split('/')[1]

        start = datetime.datetime.strptime("01-"+from_month+"-"+from_year, "%d-%m-%Y")
        end = datetime.datetime.strptime("01-"+to_month+"-"+to_year, "%d-%m-%Y")

        date_range = pd.date_range(start, end, freq='MS').strftime("%y%m").tolist()

        if date_range is None:
            exit(1)

        return date_range
    except:
        print('Especifique um periodo valido, exemplo: --dateFrom=01/2017 --dateTo=12/2017')
        exit(1)


def create_raw_files():
    if not os.path.exists(RAW_FILES_DIR):
        os.mkdir(RAW_FILES_DIR)


def create_converted_files():
    if not os.path.exists(CONVERTED_FILES_DIR):
        os.mkdir(CONVERTED_FILES_DIR)


def clean_raw_files():
    shutil.rmtree(RAW_FILES_DIR)
