from flask import Flask, jsonify
from api import data
import random


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_plan():
    return jsonify(random.choice(data.plans))


if __name__ == '__main__':
    app.run(debug=True)

