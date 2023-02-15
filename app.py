import numpy as np
import time
from collections import namedtuple
from traceback import print_exc
from pdb import set_trace
from threading import Event, Thread
from flask import Flask, render_template, request, make_response, jsonify, g
import pandas as pd
import pickle
from collections import deque

app = Flask(__name__)

# Setting CSV limit
CSV_ROW_NUM = 150

skeleton_list = []
skeleton_list_out = []
event = Event()

eval_json = {
    "evals": [
        0, 20, 40, 60, 80, 100
    ]
}

values = [0] * 50
evals = deque(values)

file = 'server_side/train_model/trained_model.pkl'
random_forest_model = pickle.load(open(file, 'rb'))


def eval_skelton():
    global eval_json
    global evals
    print('ここまでのものを評価します')
    df = pd.read_csv(r"server_side/test_data/sample.csv")
    test_x = df.drop(['action_label'], axis=1)
    predict = random_forest_model.predict(test_x)
    evals.append(predict[0])
    evals.popleft()
    eval_json["evals"] = list(evals)

    with open('server_side/tmp.txt', 'w') as f:
        for d in eval_json["evals"]:
            f.write("%s\n" % d)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/model')
def model():
    with open('eval.txt') as f:
        lines = f.readlines()

        lines = [line.rstrip('\n') for line in lines]
    global eval_json
    eval_json["evals"] = lines

    return make_response(jsonify(eval_json))


if __name__ == "__main__":

    app.run(debug=True)
