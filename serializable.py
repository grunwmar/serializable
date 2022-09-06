from abc import ABC, abstractmethod
import json


class ISerializable(ABC):
    """Serializable interface"""

    @abstractmethod
    def serialize(self): ...

    @abstractmethod
    def deserialize(self): ...

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = []
        for attr, value in self.__dict__.items():
            attributes.append(f'{attr!s}={value!r}')
        attr_string = ', '.join(attributes)
        return f'{class_name}({attr_string})'

    def __repr__(self):
        return self.__str__()


class Serializable(ABC):
    """Serializable"""

    def serialize(self, filename=None, ensure_ascii=True, indent=None):
        if filename is None:
            return json.dumps(self.__dict__)
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f, ensure_ascii=ensure_ascii, indent=indent)

    def deserialize(self, string=None, filename=None):
        if (string is not None) and (filename is not None):
            raise Exception('Cannot enter booth arguments string and filename.')
        if string is not None:
            self.__dict__ = json.loads(string)
            return self
        if filename is not None:
            with open(filename, 'r') as f:
                self.__dict__ = json.load(f)
                return self

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = []
        for attr, value in self.__dict__.items():
            attributes.append(f'{attr!s}={value!r}')
        attr_string = ', '.join(attributes)
        return f'{class_name}({attr_string})'

    def __repr__(self):
        return self.__str__()
