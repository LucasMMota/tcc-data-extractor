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


def system():
    system = get_args()['system']
    if(system is None):
        print('You should specify the datasus system')
        exit(1)

    if system in ['SIHSUS', 'SIASUS', 'SIM', 'CIH', 'CIHA', 'SINASC', 'SISPRENATAL']:
        # print('Selected system: ' + system)
        return system

    print('System: '+system+' does not exist in Datasus')
    exit(1)


def get_types():
    types = get_args()['type']
    if types is None:
        print('You should specify the database type')
        exit(1)

    system = get_args()['system']
    types = types.split(',')

    for type in types:
        if type not in DATASUS_DB_TYPES[system]:
            print('Type: '+type+' does not exist in system '+system)
            exit(1)

    # print('Selected types: ' + str(types))
    return types


def states():
    states = get_args()['states']
    states = ALL_STATES if states is None else states.split(',')

    return states


def date_from():
    date_from = get_args()['dateFrom']

    return date_from


def date_to():
    date_to = get_args()['dateTo']

    return date_to


"""
Gets range data to read available files
"""
def getDateRange():
    fromFilter = date_from()
    toFilter = date_to()

    if (fromFilter is None) or (toFilter is None):
        print('You should specify the date range, like: --dateFrom=01/2017 --dateTo=12/2017')

    fromMonth = fromFilter.split('/')[0]
    fromYear = fromFilter.split('/')[1]

    toMonth = toFilter.split('/')[0]
    toYear = toFilter.split('/')[1]

    start = datetime.datetime.strptime("01-"+fromMonth+"-"+fromYear, "%d-%m-%Y")
    end = datetime.datetime.strptime("01-"+toMonth+"-"+toYear, "%d-%m-%Y")

    dateRange = pd.date_range(start, end, freq='MS').strftime("%y%m").tolist()

    return dateRange


# todo add on filter
def getDownloadLimit():
    return 1000