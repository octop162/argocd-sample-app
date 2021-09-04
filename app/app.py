from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():
    return str(random.random())


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)