#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request, make_response, jsonify, g
import json

json_file_path = 'eval.json'

#Flaskオブジェクトの生成
app = Flask(__name__)

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    json_file_path = 'eval.json'
    result_json =0

    with open(json_file_path) as json_data:
        json_data = json.load(json_data)
        json_list = json_data['evals']
        json_list.pop(0)
        json_list.append("80")
        print(json_list)
        print(len(json_list))
        json_data['evals'] = json_list
        result_json = json_data
        # return make_response(jsonify(json_data))
    with open(json_file_path,'w') as json_data:
        json.dump(result_json,json_data,indent=4)
        return 'Hello'

#おまじない
if __name__ == "__main__":
    app.run(debug=True)
