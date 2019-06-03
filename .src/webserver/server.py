# coding=UTF-8
import sys
from flask import Flask, render_template, jsonify, request
import psycopg2
import mysql.connector
# import os
# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/datasus-downloader", methods=['POST'])
def downloader():
    sys.path.append("..")
    import extractor_script.src.datasus_downloader as datasus_downloader
    import extractor_script.src.utils as utils

    # Conversion
    input_sistema = request.form['input_sistema']
    input_de_mes = request.form['input_de_mes']
    input_de_ano = request.form['input_de_ano']
    input_ate_mes = request.form['input_ate_mes']
    input_ate_ano = request.form['input_ate_ano']

    input_tipos = request.form.getlist('input_tipo[]')
    input_tipos = input_tipos if type(input_tipos) == 'list' else [input_tipos]

    input_estados = request.form.getlist('input_estado[]')
    input_estados = input_estados if type(input_estados) == 'list' else [input_estados]

    date_range = utils.get_date_range(input_de_mes+'/'+input_de_ano, input_ate_mes+'/'+input_ate_ano)

    status = True #datasus_downloader.download_and_convert(input_sistema, date_range, input_tipos[0], input_estados[0])

    #Load DB
    input_db_type = request.form['input_db_type']
    input_db_host = request.form['input_db_host']
    input_db_port = request.form['input_db_port']
    input_db_dbname = request.form['input_db_dbname']
    input_db_user = request.form['input_db_user']
    input_db_password = request.form['input_db_password']

    if input_db_type and input_db_host and input_db_dbname and input_db_user:
        try:
            insert_data_bd(input_db_type, input_db_host, input_db_port, input_db_dbname, input_db_user, input_db_password)
        except Exception as e:
            print(e)
            return jsonify({'status': 'error', 'msg': 'Não foi possível inserir no banco. Cheque os parâmetros. '+ str(e)})

    if status:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error'})


def insert_data_bd(input_db_type, input_db_host, input_db_port, input_db_dbname, input_db_user, input_db_password):
    conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (input_db_host, input_db_dbname, input_db_user, input_db_password)
    print "Connecting to database\n	->%s" % (conn_string)

    if input_db_type == 'mysql':
        return perform_mysql(input_db_host, input_db_port, input_db_dbname, input_db_user, input_db_password)
    else:
        return perform_postgres(input_db_host, input_db_port, input_db_dbname, input_db_user, input_db_password)



def perform_mysql(input_db_host, input_db_port, input_db_dbname, input_db_user, input_db_password):
    mydb = mysql.connector.connect(
        host=input_db_host,
        user=input_db_user,
        passwd=input_db_password,
        database=input_db_dbname
    )

    mycursor = mydb.cursor(buffered=True)


    # TODO
    # Verifica se ja existe a tabela
    #   cria se necessario
    # Le CSV e insere no bd
    #   https://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python


    # mycursor.execute(
    #     """CREATE TABLE teste (
    #         id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    #         firstname VARCHAR(30) NOT NULL,
    #         lastname VARCHAR(30) NOT NULL,
    #         email VARCHAR(50),
    #         reg_date TIMESTAMP
    #     )""")
    mycursor.execute("select * from teste")


    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    # mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")



    return True


def perform_postgres(input_db_host, input_db_port, input_db_dbname, input_db_user, input_db_password):
    conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
    input_db_host, input_db_dbname, input_db_user, input_db_password)
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

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

if __name__ == "__main__":
    app.run(debug=True)

