import json

json_file_path = 'eval.json'

with open(json_file_path) as json_data:
    tmp = json.load(json_data)
    print(tmp)
    print(type(tmp))

# json_file_path = 'eval2.json'
# json_file = open(json_file_path,mode='w')
# json.dump(tmp,json_file,indent =2,ensure_ascii=False)


a = {"language": "python"}
print(type(a))
