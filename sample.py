from serializable import ISerializable, Serializable
import json


class MyClassA(Serializable):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __setattr__(self, name, value):
        super(__class__, self).__setattr__(name, value)


my_class = MyClassA()

json_string = """{
    "name": "Jeroným",
    "surname": "Hrkal",
    "age": 31
}"""

my_class.deserialize(json_string)
my_class.serialize(filename="./sample_output.json", indent=3, ensure_ascii=False)

print(my_class)

# PRINTS:
#
# MyClassA(name='Jeroným', surname='Hrkal', age=31)
#


# example of exception when abstractmethods
# defined in interface are not implemented
class MyClassB(ISerializable):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __setattr__(self, name, value):
        super(__class__, self).__setattr__(name, value)

my_class = MyClassB()

# PRINTS:
#
# Traceback (most recent call last):
#   File "/home/User/Python/Serializable/sample.py", line 45, in <module>
#     my_class = MyClassB()
#  TypeError: Can't instantiate abstract class MyClassB with abstract methods deserialize, serialize
#
