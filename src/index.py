from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <head>
    <script src="./renderer.js"></script>
    </head>
    <body>
<h1><font color="red">PythonとElectronを使ったアプリ</font></h1>
<h2><font color="blue">表示結果</font></h2>
<p>この文章は、</p>
<p>Electronでindex.jsを読み込んだあと、</p>
<p><pre>「require('child_process').spawn('python',['./index.py']);」</pre></p>
<p>によって、index.pyファイルを読み込み表示した文章です。</p>
<form action="/" method='GET'>
    <input type="submit" value="REFRESH">
</form>
</body>



"""


if __name__ == "__main__":
    # debug モードで起動
    app.run(debug=True, host="localhost", port=5000)