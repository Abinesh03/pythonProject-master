import json

# some JSON:
#x =  '{ "name":"Abinesh", "age":27, "city":"Chennai"}'

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:
#print(y["name"])

# a Python object (dict):
x = {
  "name": "Abinesh",
  "age": 27,
  "city": "Chennai"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)