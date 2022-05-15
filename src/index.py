from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bootstrap")
def bootstrap():
    return  render_template("bootstrap.html")


if __name__ == "__main__":
    # debug モードで起動
    app.run(debug=True, host="localhost", port=5000)
