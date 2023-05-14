from bcbcpy.__ import __author__


from bcbcpy.crypto.key import SymmetricKey
from bcbcpy.utils import C2I, I2C, TOTAL_CHAR


import random

__all__ = ["CaesarKey", "caesar_encoder"]


class CaesarKey(SymmetricKey):
    def __init__(self, key_value: int) -> None:
        super().__init__(key_value, caesar_encoder)

    def __repr__(self) -> str:
        return f"CaesarKey({self._first.key_value})"

    @classmethod
    def compute_inverse(cls, key_value: int) -> int:
        new_value = -key_value
        return new_value

    @staticmethod
    def generate_key(max_length: int = TOTAL_CHAR) -> "CaesarKey":
        key = random.randint(1, max_length)
        return CaesarKey(key)


def caesar_encoder(text: str, key_value: int) -> str:
    encoded_text = ""
    for c in text:
        encoded_text += I2C[(C2I[c] + key_value) % TOTAL_CHAR]
    return encoded_text
