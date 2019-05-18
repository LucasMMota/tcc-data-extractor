import sys
import argparse
from .constants import DATASUS_DB_TYPES, ALL_STATES
import datetime
import pandas as pd

def get_args():
    # initiate the parser
    parser = argparse.ArgumentParser()

    # add long and short argument
    parser.add_argument("--system", help="...")
    parser.add_argument("--dateFrom", help="...")
    parser.add_argument("--dateTo", help="...")
    parser.add_argument("--states", help="...")
    parser.add_argument("--type", help="...")

    # read arguments from the command line
    args = parser.parse_args()

    return {
        'system': args.system.upper() if (args.system is not None) else None,
        'type': args.type.upper() if (args.type is not None) else None,
        'dateFrom': args.dateFrom,
        'dateTo': args.dateTo,
        'states': args.states,
    }


def get_system():
    system = get_args()['system']
    if(system is None):
        print('Esepecifique o sistema')
        exit(1)

    if system in ['SIHSUS', 'SIASUS', 'SIM', 'CIH', 'CIHA', 'SINASC', 'SISPRENATAL']:
        # print('Selected system: ' + system)
        return system

    print('System: '+system+' does not exist in Datasus')
    exit(1)


def get_types():
    types = get_args()['type']
    if types is None:
        print('Especifique o tipo de arquivos')
        exit(1)

    system = get_system()
    types = types.split(',')

    for type in types:
        if type not in DATASUS_DB_TYPES[system]:
            print('Tipo: '+type+' nao existe no sistema '+system)
            exit(1)

    # print('Selected types: ' + str(types))
    return types


def get_states():
    states = get_args()['states']

    states = ALL_STATES if states is None else states.split(',')

    if ALL_STATES != states:
        for uf in states:
            if uf not in ALL_STATES:
                print('Estado(s): ' + uf + ' invalido')
                exit(1)

    return states


def date_from():
    date = get_args()['dateFrom']
    if date is None:
        print('Especifique um dateFrom valido, exemplo: --dateFrom=01/2017')
        exit(1)

    return date


def date_to():
    date = get_args()['dateTo']
    if date is None:
        print('Especifique um dateTo valido, exemplo: --dateTo=12/2017')
        exit(1)

    return date


# Gets range data to read available files
def get_date_range():
    try:
        from_filter = date_from()
        to_filter = date_to()

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


# todo add on filter
# def get_download_limit():
#     return 1000


def get_filters():
    system = get_system()
    file_types = get_types()
    states = get_states()
    date_range = get_date_range()

    return system, date_range, file_types, states
