from bcbcpy.__ import __author__


from typing import Callable, Any, Iterator

__all__ = [
    "BaseKey",
    "BasePairKeys",
    "BaseSymmetricKey",
    "BaseAsymmetricKeys",
]


class BaseKey:
    def __init__(self, key_value, encoder: Callable[[str, Any], str]) -> None:
        self.key_value = key_value
        self._enc_fct = encoder

    def __repr__(self) -> str:
        return str(self.key_value)

    def encode(self, text: str) -> str:
        return self._enc_fct(text, self.key_value)

    def key_alike(self, key_value) -> "BaseKey":
        assert isinstance(key_value, type(self.key_value))
        return type(self)(key_value, self._enc_fct)


class BasePairKeys:
    def __init__(self, first: BaseKey, second: BaseKey) -> None:
        self._first = first
        self.__sec = second

    def __iter__(self) -> Iterator[BaseKey]:
        return iter([self._first, self.__sec])

    @property
    def pub(self) -> BaseKey:
        return self._first

    def encrypt(self, txt: str) -> str:
        return self._first.encode(txt)

    def decrypt(self, txt: str) -> str:
        return self.__sec.encode(txt)

    def sign(self, txt: str) -> str:
        return self.decrypt(txt)


class BaseSymmetricKey(BasePairKeys):
    def __init__(self, key_value, encoder: Callable[[str, Any], str]) -> None:
        inverse = self.compute_inverse(key_value)

        first = BaseKey(key_value, encoder)
        second = BaseKey(inverse, encoder)
        super().__init__(first, second)

    def __repr__(self) -> str:
        self__sec_key_value = self.compute_inverse(self._first.key_value)
        if self._first.key_value == self__sec_key_value:
            return f"{self.__class__.__name__}({self._first})"
        else:
            return f"{self.__class__.__name__}({self._first.key_value}, {self__sec_key_value})"

    @staticmethod
    def compute_inverse(key_value: Any):
        return key_value

    @staticmethod
    def generate_key():
        raise NotImplementedError


class BaseAsymmetricKeys(BasePairKeys):
    def __init__(self, pub: BaseKey, priv: BaseKey) -> None:
        super().__init__(first=pub, second=priv)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._first}, HIDDEN_KEY)"

    @staticmethod
    def generate_pairs():
        raise NotImplementedError
