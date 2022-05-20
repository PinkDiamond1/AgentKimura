from flask import Flask, render_template
from io import BytesIO
import matplotlib
import urllib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")


@app.route("/getOrderBook")
def get_order_book():
    data = {'symbol': 'BTC/JPY', 'bids': [[3826050.0, 0.0002], [3825926.0, 0.01], [3825837.0, 0.00261294], [3825229.0, 0.095], [3824984.0, 0.04357494], [3824739.0, 0.01541357], [3824666.0, 0.001], [3824624.0, 0.01073233], [3824433.0, 0.01], [3824432.0, 0.095], [3824207.0, 0.02164], [3824162.0, 0.0066], [3824160.0, 0.109], [3824070.0, 0.15], [3823557.0, 0.044], [3823360.0, 0.002], [3823236.0, 0.001], [3823077.0, 0.5], [3822537.0, 0.01], [3822012.0, 0.04], [3821742.0, 0.31]], 'asks': [[3826935.0, 0.005], [3827223.0, 0.15], [3827464.0, 0.03607379], [3827470.0, 0.0375936], [3827476.0, 0.01880214], [3827481.0, 0.095], [3827482.0, 0.095], [3827611.0, 0.095], [3828079.0, 0.0055], [3828270.0, 0.011], [3828552.0, 0.002], [3828570.0, 0.10687576], [3828661.0, 0.31], [3828682.0, 0.095], [3829078.0, 0.0002], [3829093.0, 0.001], [3829304.0, 0.01], [3829345.0, 0.36901978], [3829346.0, 0.001], [3829476.0, 0.17], [3829962.0, 0.00752133]], 'timestamp': None, 'datetime': None, 'nonce': None}

    fig, ax = plt.subplots(1, 1)
    sum = 0
    for i in data["bids"]:
        sum += i[1]
        i.append(sum)

    column_labels = ["Price", "AMount", "Sum"]
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data["bids"], colLabels=column_labels, loc="center")
    canvas = FigureCanvasAgg(fig)
    buf = BytesIO()
    canvas.print_png(buf)
    d = buf.getvalue()
    img_data = urllib.parse.quote(d)
    return img_data


@app.route("/exchange")
def exchange():
    data = {'symbol': 'BTC/JPY', 'bids': [[3826050.0, 0.0002], [3825926.0, 0.01], [3825837.0, 0.00261294], [3825229.0, 0.095], [3824984.0, 0.04357494], [3824739.0, 0.01541357], [3824666.0, 0.001], [3824624.0, 0.01073233], [3824433.0, 0.01], [3824432.0, 0.095], [3824207.0, 0.02164], [3824162.0, 0.0066], [3824160.0, 0.109], [3824070.0, 0.15], [3823557.0, 0.044], [3823360.0, 0.002], [3823236.0, 0.001], [3823077.0, 0.5], [3822537.0, 0.01], [3822012.0, 0.04], [3821742.0, 0.31]], 'asks': [[3826935.0, 0.005], [3827223.0, 0.15], [3827464.0, 0.03607379], [3827470.0, 0.0375936], [3827476.0, 0.01880214], [3827481.0, 0.095], [3827482.0, 0.095], [3827611.0, 0.095], [3828079.0, 0.0055], [3828270.0, 0.011], [3828552.0, 0.002], [3828570.0, 0.10687576], [3828661.0, 0.31], [3828682.0, 0.095], [3829078.0, 0.0002], [3829093.0, 0.001], [3829304.0, 0.01], [3829345.0, 0.36901978], [3829346.0, 0.001], [3829476.0, 0.17], [3829962.0, 0.00752133]], 'timestamp': None, 'datetime': None, 'nonce': None}

    fig, ax = plt.subplots(1, 1)
    sum = 0
    for i in data["bids"]:
        sum += i[1]
        i.append(sum)

    column_labels = ["Price", "AMount", "Sum"]
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data["bids"], colLabels=column_labels, loc="center")
    canvas = FigureCanvasAgg(fig)
    buf = BytesIO()
    canvas.print_png(buf)
    d = buf.getvalue()
    img_data = urllib.parse.quote(d)
    return render_template("exchange.html", img_data=img_data)


if __name__ == "__main__":
    # debug モードで起動
    app.run(debug=True, host="localhost", port=5000)
