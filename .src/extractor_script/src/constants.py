# coding=utf-8
from os.path import dirname, abspath

RAW_FILES_DIR = dirname(dirname(abspath(__file__)))+'/raw-files/'
ERROR_LOG_FILES_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))+'/'
SRC_DIR = (dirname(abspath(__file__)))
CONVERTED_FILES_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))+'/dados/' # todo mudar no doc o converted-files de staging etc pros novos nomes

"""
    SIHSUS
        RD - AIH Reduzida
        RJ - AIH Rejeitadas
        SP - Serviços Profissionais
        ER - AIH Rejeitadas

    SIASUS
        AB - APAC de Acompanhamento a Cirurgia Bariatrica - A Partir de Jan/2008 ate Mar/2013
        ABO - APAC Acompanhamento Pós Cirurgia Bariatrica - A Partir de Abr/2013
        ACF - APAC Confeção de Fístula Arteriovenosa - A Partir de Jun/2014
        AD - APAC de Laudos Diversos - A Partir de Jan/2008
        AM - APAC de Medicamentos - A Partir de Jan/2008
        AN - APAC de Nefrologia - A Partir de Jan/2008 até Out/2014
        AQ - APAC de Quimioterapia - A Partir de Jan/2008
        AR - APAC de Radioterapia - A Partir de Jan/2008
        ATD - APAC Tratamento Dialítico - A Partir de Jun/2014
        PA - Produção Ambulatorial - A Partir de Jul/1994
        PS - Psicossocial - A Partir de Jan/2013
        SAD - Atenção Domiciliar - A Partir de Nov/2012</option>

    SIM
        DOP - Declarações de Óbito - 2017 preliminar
        DO - Declarações de Óbito - 1979 a 2016
        DOFETP - Declarações de Óbitos fetais - 2017 preliminar
        DOFET - Declarações de Óbitos fetais - 1979 a 2016
        DOEXTP - Declarações de Óbitos por causas externas - 2017 preliminar
        DOEXT - Declarações de Óbitos por causas externas - 1979 a 2016
        DOINFP - Declarações de Óbitos infantis - 2017 preliminar
        DOINF - Declarações de Óbitos infantis - 1979 a 2016
        DOMATP - Declarações de Óbitos maternos - 2017 preliminar
        DOMAT - Declarações de Óbitos maternos - 1996 a 2016</option>

    CIH
        CR - Comunicação de Internação Hospitalar - A partir de Jan/2008

    CIHA
        CIHA - Comunicação de Internação Hospitalar e Ambulatorial - A partir de Jan/2011

    SINASC
        DN - Declarações de nascidos vivos 1994 a 2016
        DNP - Declarações de nascidos vivos 2017 preliminar

    SISPRENATAL
        PN - Pré-Natal
"""
DATASUS_DB_TYPES = {
    'SIHSUS': ['RD', 'RJ', 'SP', 'ER'],
    'SIASUS': ['AB', 'ABO', 'ACF', 'AD', 'AM', 'AN', 'AQ', 'AR', 'ATD', 'PA', 'PS', 'SAD'],
    'CIH': ['CR'],
    'CIHA': ['CIHA'],
    'SISPRENATAL': ['PN']
    # todo analisar estrutura de arquivos['DOFETP', 'DOFET', 'DOEXTP', 'DOEXT', 'DOINFP', 'DOINF', 'DOMATP', 'DOMAT'],
    # 'SIM': ['DOP', 'DO'],
    # 'SINASC': ['DN', 'DNP'],
}

DATASUS_SYSTEM_PATHS = {
    'SIHSUS': '/dissemin/publicos/SIHSUS/200801_/dados/',
    'SIASUS': '/dissemin/publicos/SIASUS/200801_/Dados/',
    'CIH': '/dissemin/publicos/CIH/200801_201012/Dados/',
    'CIHA': '/dissemin/publicos/CIHA/201101_/Dados/',
    'SISPRENATAL': '/dissemin/publicos/SISPRENATAL/201201_/Dados/',
    # 'SIM': '/dissemin/publicos/SIM/PRELIM/DOFET/',
    #'SINASC': '/dissemin/publicos/SINASC/NOV/DNRES/', # todo por ano
}

# Todo: mapear range de data pra cada tipo fara facilitar o retorno ao usuario
# DB_TYPES_DATE_RANGE_AVAILABLE={}

ALL_STATES = {
    "AC",
    "AL",
    "AM",
    "AP",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MG",
    "MS",
    "MT",
    "PA",
    "PB",
    "PE",
    "PI",
    "PR",
    "RJ",
    "RN",
    "RO",
    "RR",
    "RS",
    "SC",
    "SE",
    "SP",
    "TO",
}
