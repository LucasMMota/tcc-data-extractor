# coding=UTF-8
import sys
from flask import Flask, render_template, jsonify, request
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

    input_db_type = ''
    if 'input_db_type' in request.form:
        input_db_type = request.form['input_db_type']
    input_db_host = request.form['input_db_host']
    input_db_dbname = request.form['input_db_dbname']
    input_db_user = request.form['input_db_user']
    input_db_password = request.form['input_db_password']

    status = datasus_downloader.download_and_convert(input_sistema, date_range, input_tipos[0], input_estados[0], input_db_type, input_db_host, input_db_dbname, input_db_user, input_db_password)

    # if input_db_type and input_db_host and input_db_dbname and input_db_user:
    #     try:
    #         database_insert.insert_on_bd(input_db_type, input_db_host, input_db_dbname, input_db_user, input_db_password, input_sistema, filename)
    #     except Exception as e:
    #         print(e)
    #         return jsonify({'status': 'error', 'msg': 'Não foi possível inserir no banco. Cheque os parâmetros. '+ str(e)})

    if status is True:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error'})


if __name__ == "__main__":
    app.run(debug=True)

