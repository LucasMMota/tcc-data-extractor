import sys
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/datasus-downloader")
def downloader():
    sys.path.append("..")
    import extractor_script.src.datasus_downloader as datasus_downloader
    import extractor_script.src.utils as utils

    date_range = utils.get_date_range('02/2017', '02/2017')
    datasus_downloader.download_and_convert("SIASUS", date_range, ["AB"], ["SP"])

    # executa e grava do dir de convertidos
    # falta colocar loader
    #  retornar uma msg de instrucao

    return jsonify({'status': 'success'})


if __name__ == "__main__":
    app.run(debug=True)

