from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><img src=\"http://i.imgur.com/KSGHCUs.gif\"></body></html>"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
