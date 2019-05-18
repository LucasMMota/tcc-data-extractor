import os
import shutil
from constants import RAW_FILES_DIR, CONVERTED_FILES_DIR, DATASUS_SYSTEM_PATHS


def build_file_path(system, file_type, date, state):
    path = DATASUS_SYSTEM_PATHS[system]
    filename = file_type + state + date + '.dbc'

    return path, filename


def create_raw_files():
    if not os.path.exists(RAW_FILES_DIR):
        os.mkdir(RAW_FILES_DIR)


def create_converted_files():
    if not os.path.exists(CONVERTED_FILES_DIR):
        os.mkdir(CONVERTED_FILES_DIR)


def clean_raw_files():
    shutil.rmtree(RAW_FILES_DIR)