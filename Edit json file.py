import json


def file_read():
    with open("Names.json", "r") as json_file:
        data = json.load(json_file)
        temp = data["names"]
    return temp

def file_write(json_object):
    with open("Names1.json", "w") as f:
        json.dump(json_object,f,indent=4)


def task(temp):
    y = {"name": "abi","age": 26}
    temp.append(y)
    return temp


if __name__ == '__main__':
    a = file_read()
    b = task(temp=a)
    file_write(json_object=b)


# with open("Names.json", "r") as json_file:
#     data = json.load(json_file)
#     temp = data["names"]
#     print(temp)
#     print(type(temp))
#     y = {"name":"Elango","age": 26}
#     temp.append(y)
#     print(temp)
#     with open("Names1.json", "w") as f:
#         json.dump(temp,f,indent=4)

