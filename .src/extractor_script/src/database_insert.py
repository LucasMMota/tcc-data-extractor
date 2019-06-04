# -*- coding: utf-8 -*-
from constants import CONVERTED_FILES_DIR
import csv
import re


def insert_on_bd(input_db_type, input_db_host, input_db_dbname, input_db_user, input_db_password, input_sistema, filename):
    if input_db_type == 'mysql':
        return perform_mysql(input_db_host, input_db_dbname, input_db_user, input_db_password, input_sistema, filename)
    else:
        return perform_postgres(input_db_host, input_db_dbname, input_db_user, input_db_password, input_sistema, filename)


def table_exists(mysql_conn, tablename):
    try:
        dbcur = mysql_conn.cursor(buffered=True)
        dbcur.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))

        status = False
        if dbcur.fetchone()[0] == 1:
            status = True

        dbcur.close()
        return status
    except:
        return False


def build_table_name(filename, dsus_system):
    tablename = dsus_system + "_" + filename[:-14]
    return tablename


def build_fields_names(arr_fieldnames):
    str_fieldnames = ''
    # print(arr_fieldnames)
    for fieldname in arr_fieldnames:
        str_fieldnames += fieldname + ' TEXT,'

    return str_fieldnames[:-1]


def create_table(conn, tablename, arr_fieldnames):
    stmt = """CREATE TABLE {0} (
                id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
                {1}
                )
            """.format(tablename.replace('\'', '\'\''), build_fields_names(arr_fieldnames))
    # print(stmt)
    try:
        dbcur = conn.cursor(buffered=True)
        dbcur.execute(stmt)
        conn.commit()
        dbcur.close()
    except Exception as e:
        print("failed to execute!")
        print(e)
        return False

    return True


def create_table_if_not_exists(mysql_conn, tablename, arr_fieldnames):
    print('#### TABLENAME ' + tablename)
    if not table_exists(mysql_conn, tablename):
        return create_table(mysql_conn, tablename, arr_fieldnames)
    return True


def build_fields_to_insert(arr_fieldnames):
    str_fields = ''
    for field in arr_fieldnames:
        str_fields += field + ','
    str_fields = str_fields[:-1]

    return str_fields


def build_values_to_insert(dict_values):
    str_values = ''
    for value in dict_values.values():
        value = re.sub(r'[^\x00-\x7f]', r'', value)
        str_values += '\''+ value + '\','
    str_values = str_values[:-1]

    return str_values


def get_file_rows(filename):
    with open(CONVERTED_FILES_DIR + filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        num = sum(1 for _row in reader)
        return num
    raise Exception('Erro ler tamanho do CSV para inserir no banco.')


def insert_csv_into_db(mysql_conn, filename, tablename, arr_fieldnames):
    with open(CONVERTED_FILES_DIR+filename) as csvfile:
        try:
            str_fields = build_fields_to_insert(arr_fieldnames)
            row_count = get_file_rows(filename)
            batch_stmt = 'INSERT INTO {0} ({1}) VALUES '.format(tablename.replace('\'', '\'\''), str_fields)
            batch = 0
            counter = 0
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                str_values = build_values_to_insert(row)
                stmt = " ({0}),".format(str_values)
                batch_stmt += stmt
                batch +=1
                counter +=1
                if (batch == 300) or (counter == row_count):
                    batch_stmt = batch_stmt[:-1] + ';'
                    # print('stmbatch='+batch_stmt)
                    cur = mysql_conn.cursor(buffered=True)
                    cur.execute(batch_stmt)
                    mysql_conn.commit()
                    cur.close()
                    batch = 0
                    # print('batchstm='+batch_stmt[:3000])
                    batch_stmt = 'INSERT INTO {0} ({1}) VALUES '.format(tablename.replace('\'', '\'\''), str_fields)
            return True
        except Exception as e:
            print(e)
            return False


def get_field_names_from_csv(filename):
    with open(CONVERTED_FILES_DIR+filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        arr_fields_names = []
        for row in reader:
            i = 1
            for field in row:
                if (not field):
                    field = 'unnamed_col_' + str(i)
                    i += 1
                field = '`'+field+'`'
                arr_fields_names.append(field)
            return arr_fields_names
    raise Exception('Erro ao pegar nomes dos campos do CSV para inserir no banco.')


def perform_mysql(input_db_host, input_db_dbname, input_db_user, input_db_password, dsus_system, filename):
    import mysql.connector
    import mysql

    mysql_conn = mysql.connector.connect(
        host=input_db_host,
        user=input_db_user,
        passwd=input_db_password,
        database=input_db_dbname
    )

    tablename = build_table_name(filename, dsus_system)
    arr_fieldnames = get_field_names_from_csv(filename)
    create_table_if_not_exists(mysql_conn, tablename, arr_fieldnames)
    insert_csv_into_db(mysql_conn, filename, tablename, arr_fieldnames)

    return True


def perform_postgres(input_db_host, input_db_port, input_db_dbname, input_db_user, input_db_password, filename):
    import psycopg2

    conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
    input_db_host, input_db_dbname, input_db_user, input_db_password)
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor(buffered=True)

    # execute our Query
    cursor.execute("SELECT * FROM my_table")

    # retrieve the records from the database
    records = cursor.fetchall()

    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    print(records)
    return True


# insert_on_bd('mysql', '127.0.0.1', 'tcc', 'root', '', 'SIHSUS', 'ABOES1801.dbc.csv')