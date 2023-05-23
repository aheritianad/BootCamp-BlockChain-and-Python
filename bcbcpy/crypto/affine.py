from bcbcpy.__ import __author__


from bcbcpy.crypto.basekey import BaseSymmetricKey
from bcbcpy.utils import C2I, I2C, TOTAL_CHAR
from bcbcpy.math.arithmetic import inverse_mod
from typing import Tuple


import random

__all__ = ["AffineKey", "affine_encoder"]


def affine_encoder(text: str, key_value: Tuple[int, int]) -> str:
    a, b = key_value
    encoded_text = ""
    for c in text:
        x = C2I[c]
        encoded_text += I2C[(a * x + b) % TOTAL_CHAR]
    return encoded_text


class AffineKey(BaseSymmetricKey):
    def __init__(self, key_value: Tuple[int, int] = (1, 0)) -> None:
        if inverse_mod(key_value[0], TOTAL_CHAR) is None:
            raise ValueError(
                f"Invalid key value. First element needs to be invertible mod {TOTAL_CHAR}."
            )
        super().__init__(key_value, affine_encoder)

    def __repr__(self) -> str:
        return f"AffineKey({self._first.key_value[0]},{self._first.key_value[1]})"

    @staticmethod
    def compute_inverse(key_value: Tuple[int, int]) -> Tuple[int, int]:
        a = inverse_mod(key_value[0], TOTAL_CHAR)
        if a is None:
            raise ValueError(
                f"Invalid key value. First element needs to be invertible mod {TOTAL_CHAR}."
            )
        b = (-a * key_value[1]) % TOTAL_CHAR
        return (a, b)

    @staticmethod
    def generate_key() -> "AffineKey":
        while True:
            a = random.randint(1, TOTAL_CHAR - 1)
            if inverse_mod(a, TOTAL_CHAR) is not None:
                break
        b = random.randint(1, TOTAL_CHAR - 1)
        key_value = (a, b)
        return AffineKey(key_value)
