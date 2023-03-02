import numpy as np
import time
import json
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

model_file = 'model/trained_model.pkl'
random_forest_model = pickle.load(open(model_file, 'rb'))

json_path = 'eval.json'
def eval_skelton():
    global eval_json
    df = pd.read_csv(r"test_data/sample.csv")
    test_x = df.drop(['action_label'], axis=1)
    predict = random_forest_model.predict(test_x)

    with open(json_path) as f:
        json_data = json.load(f)
        print(json_data)
        print(type(json_data))
        return json_data
        # pre_data = deque(json_data['evals'])
        # pre_data.append(predict[0])
        # pre_data.popleft()
        # print('----------------------------')
        # print(pre_data)
        # list_data = list(pre_data)
        # print(list_data)
        # json_data['evals'] = list_data
        # return json_data

@app.route('/')
def index():
    return 'Hello World'


@app.route('/model')
def return_json():
    # modelで評価
    json_data = eval_skelton()
    with open(json_path, 'w') as file:
        json.dump(json_data, file, indent=2)

    with open('eval.json') as f:
        return make_response(jsonify(json_data))

if __name__ == "__main__":
    app.run(debug=True)
