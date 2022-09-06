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
    """Serializable. Like ISerializable but has serialize and deserialize already implemented."""

    def serialize(self, filename: str=None, ensure_ascii: bool=True, indent: bool=None):
        if filename is None:
            return json.dumps(self.__dict__)
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f, ensure_ascii=ensure_ascii, indent=indent)

    def deserialize(self, string: str=None, filename: str=None):
        if (string is not None) and (filename is not None):
            raise Exception('Cannot enter both arguments string and filename.')
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
