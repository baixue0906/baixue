import json

inData = '{"opterToken": "123"}'
print(json.loads(inData)['opterToken'])