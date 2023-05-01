from bcbcpy import __author__


from typing import Callable, Any

__all__ = [
    "convert",
    "Key",
    "BaseKeys",
    "SymmetricKey",
    "AsymmetricKeys",
]


class Key:
    def __init__(self, key_value, convert: Callable[[str, Any], str]):
        self.key_value = key_value
        self._conv_fcs = convert

    def __str__(self):
        return str(self.key_value)

    def convert(self, text: str):
        return self._conv_fcs(text, self.key_value)

    def key_alike(self, key_value):
        assert isinstance(key_value, type(self.key_value))
        return type(self)(key_value, self._conv_fcs)


def convert(text: str, key: Key):
    return key.convert(text)


class BaseKeys:
    def __init__(self, first: Key, second: Key):
        self._first = first
        self.__sec = second

    def __iter__(self):
        return iter([self._first, self.__sec])

    @property
    def pub(self):
        return self._first

    def encrypt(self, txt: str):
        return self._first.convert(txt)

    def decrypt(self, txt: str):
        return self.__sec.convert(txt)

    def sign(self, txt: str):
        return self.__sec.convert(txt)


class SymmetricKey(BaseKeys):
    def __init__(self, key_value, convert: Callable[[str, Any], str]):
        inverse = self.compute_inverse(key_value)

        first = Key(key_value, convert)
        second = Key(inverse, convert)

        super().__init__(first, second)

    def __repr__(self):
        self__sec_key_value = self.compute_inverse(self._first.key_value)
        if self._first.key_value == self__sec_key_value:
            return f"{self.__class__.__name__}({self._first})"
        else:
            return f"{self.__class__.__name__}({self._first.key_value}, {self__sec_key_value})"

    @classmethod
    def compute_inverse(cls, key_value: Any):
        return key_value

    @staticmethod
    def generate_key():
        raise NotImplementedError


class AsymmetricKeys(BaseKeys):
    def __init__(self, pub: Key, priv: Key):
        super().__init__(first=pub, second=priv)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._first}, HIDDEN_KEY)"

    @staticmethod
    def generate_pairs():
        raise NotImplementedError
