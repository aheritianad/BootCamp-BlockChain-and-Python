from bcbcpy import __author__


from bcbcpy.crypto.key import Key, SymmetricKey


from typing import Tuple, Callable, Any
import random


__all__ = ["PermutationKey", "permute_convert", "permute"]


class PermutationKey(SymmetricKey):
    def __init__(self, key_value: Tuple[int, ...], n_runs: int = 2):
        super().__init__(key_value, permute_convert(n_runs))

    def __repr__(self):
        return (
            f"PermutationKey({self._first.key_value}, {self._BaseKeys__sec.key_value})"
        )

    def compute_inverse(self, key_value: Tuple[int, ...]):
        new_value = [0] * len(key_value)
        for i, image in enumerate(key_value):
            new_value[image - 1] = i + 1
        new_value = tuple(new_value)
        return new_value

    @staticmethod
    def generate_key(length: int = 5, n_runs: int = 2):
        pub = list(range(1, length + 1))
        random.shuffle(pub)
        pub = tuple(pub)
        return PermutationKey(pub, n_runs)


def permute(text: str, key_value: Tuple[int, ...]):
    converted_text = ""
    n = len(key_value)
    lt = len(text)
    for i in range(0, lt // n):
        start = i * n
        for k in key_value:
            converted_text += text[start + k - 1]
    return converted_text + text[n * (lt // n) :]


def permute_convert(n: int = 2):
    assert n == 1 or n % 2 == 0, "n needs to be 1 or an evn number."

    def _permute(text: str, key_value: Tuple[int, ...]):
        for _ in range(n):
            text = permute(text, key_value)[::-1]
        return text[::-1]

    return _permute