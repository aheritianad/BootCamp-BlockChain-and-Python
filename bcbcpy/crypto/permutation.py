from bcbcpy.__ import __author__


from bcbcpy.crypto.basekey import BaseSymmetricKey

from typing import List, Callable


import random


__all__ = ["PermutationKey", "permutation_encoder", "permute"]


class PermutationKey(BaseSymmetricKey):
    def __init__(self, key_value: List[int], n_runs: int = 2) -> None:
        super().__init__(key_value, permutation_encoder(n_runs))

    def __repr__(self):
        return f"PermutationKey({self._first.key_value})"

    @staticmethod
    def compute_inverse(key_value: List[int]) -> list[int]:
        new_value = [0] * len(key_value)
        for i, image in enumerate(key_value):
            new_value[image - 1] = i + 1
        return new_value

    @staticmethod
    def generate_key(length: int = 5, n_runs: int = 2) -> "PermutationKey":
        pub = list(range(1, length + 1))
        random.shuffle(pub)
        return PermutationKey(pub, n_runs)


def permute(text: str, key_value: List[int]) -> str:
    encoded_text = ""
    n = len(key_value)
    lt = len(text)
    for i in range(0, lt // n):
        start = i * n
        for k in key_value:
            encoded_text += text[start + k - 1]
    return encoded_text + text[n * (lt // n) :]


def permutation_encoder(n: int = 2) -> Callable[[str, List[int]], str]:
    assert n == 1 or n % 2 == 0, "n needs to be 1 or an evn number."

    def _permute(text: str, key_value: List[int]) -> str:
        for _ in range(n):
            text = permute(text, key_value)[::-1]
        return text[::-1]

    return _permute
