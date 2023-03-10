import numpy as np
import json
from collections import namedtuple
from traceback import print_exc
from pdb import set_trace
from threading import Event, Thread
from flask import Flask, render_template, request, make_response, jsonify, g
import pandas as pd
import pickle
from collections import deque
from dotenv import load_dotenv
import boto3

app = Flask(__name__)

# Setting CSV limit
CSV_ROW_NUM = 150

model_file = 'model/trained_model.pkl'
random_forest_model = pickle.load(open(model_file, 'rb'))
json_path = 'eval.json'


def download_csv():
    load_dotenv()
    Bucket = 'm1gp-mishima'
    Key = 'test.csv'
    Filename = 'test_data/test.csv'
    s3 = boto3.resource('s3')
    s3.Bucket(Bucket).download_file(Filename=Filename, Key=Key)


def eval_skelton():
    global eval_json
    df = pd.read_csv(r"test_data/test.csv")
    test_x = df.drop(['action_label'], axis=1)
    predict = random_forest_model.predict(test_x)

    # json読み込み
    with open(json_path) as f:
        json_data = json.load(f)
        json_list = json_data['evals']
        json_list.pop(0)
        json_list.append(str(predict[0]))
        json_data['evals'] = json_list
        result_json = json_data
    # jsonに書き込み
    with open(json_path, 'w') as json_data:
        json.dump(result_json, json_data, indent=4)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/model')
def return_json():
    # 最新の骨格情報を取得
    download_csv()
    # modelで評価
    eval_skelton()
    
    with open('eval.json') as f:
        json_data = json.load(f)
        return make_response(jsonify(json_data))

if __name__ == "__main__":
    app.run(debug=True)
