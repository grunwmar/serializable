from serializable import ISerializable, Serializable
import json


class MyClass(Serializable):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __setattr__(self, name, value):
        super(__class__, self).__setattr__(name, value)



my_class = MyClass()

json_string = """{
    "name": "Jeroným",
    "surname": "Hrkal",
    "age": 31
}"""

my_class.deserialize(json_string)

print(my_class)

my_class.serialize(filename="./sample_output.json", indent=3, ensure_ascii=False)
