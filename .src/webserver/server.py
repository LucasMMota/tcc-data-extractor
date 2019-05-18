from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# import webbrowser
#
# a_website = "https://www.google.com"
#
# # Open url in a new window of the default browser, if possible
# webbrowser.open_new(a_website)