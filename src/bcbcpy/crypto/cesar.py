from bcbcpy import __author__


from bcbcpy.crypto.key import SymmetricKey
from bcbcpy.utils import C2I, I2C, TOTAL_CHAR


import random

__all__ = ["CesarKey", "cesar_convert"]


class CesarKey(SymmetricKey):
    def __init__(self, key_value: int):
        super().__init__(key_value, cesar_convert)

    def __repr__(self):
        return f"CesarKey({self._first.key_value}, {self._BaseKeys__sec.key_value})"

    def compute_inverse(self, key_value: int):
        new_value = -key_value
        return new_value

    @staticmethod
    def generate_key(max_length: int = TOTAL_CHAR):
        key = random.randint(1, max_length)
        return CesarKey(key)


def cesar_convert(text: str, key_value: int) -> str:
    converted_text = ""
    for c in text:
        converted_text += I2C[(C2I[c] + key_value) % TOTAL_CHAR]
    return converted_text
