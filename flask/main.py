from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/series")
def series():
    return pd.Series([1, 3, 4, 5, 6, 8]).to_json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6677)
