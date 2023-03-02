import json

json_file_path = 'eval.json'

with open(json_file_path) as json_data:
    tmp = json.load(json_data)
    print(tmp)
    print(type(tmp))

a = {"language": "python"}
print(type(a))
