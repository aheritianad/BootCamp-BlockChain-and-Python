from bcbcpy.__ import __author__


from bcbcpy.crypto import Key, AsymmetricKeys
from bcbcpy.math import (
    inverse_mod,
    int2base,
    base2int,
    generate_probably_prime,
)
from bcbcpy.utils import TOTAL_CHAR, txt2int, int2txt


from typing import Tuple
import random

__all__ = [
    "RSAKey",
    "RSAPairKeys",
    "rsa_encoder",
]


def rsa_encoder(txt: str, key_value: Tuple[int, int]) -> str:
    n, e = key_value
    assert n > TOTAL_CHAR, "Key too small."
    base_10 = txt2int(txt)
    base_n = int2base(base_10, n)
    cip_n = [pow(digit, e, n) for digit in base_n]
    cip_10 = base2int(cip_n, n)
    out = int2txt(cip_10)
    return out


class RSAKey(Key):
    def __init__(self, key_value: Tuple[int, int]) -> None:
        encoder = lambda txt, key_value: rsa_encoder(txt, key_value)
        super().__init__(
            key_value,
            encoder,
        )


class RSAPairKeys(AsymmetricKeys):
    def __init__(self, pub: RSAKey, priv: RSAKey) -> None:
        super().__init__(pub, priv)

    def __repr__(self) -> str:
        return f"RSAPairKeys({self._first}, HIDDEN_KEY)"

    @staticmethod
    def generate_pairs(bit_size: int = 16) -> "RSAPairKeys":
        assert bit_size > 4
        b = bit_size // 2 + 1
        p = generate_probably_prime(bit_size // 2 + 1)
        q = generate_probably_prime(bit_size // 2 - 1)
        n = p * q
        phi = (p - 1) * (q - 1)

        ds = list(range(phi // 4, 3 * phi // 4))
        random.shuffle(ds)

        for d in ds:
            e = inverse_mod(d, phi)
            if e:  # e exist (not None)
                break
        else:
            d = e = phi - 1  # not supposed to happened, but I still put it for security

        pub = RSAKey(key_value=(n, d))
        priv = RSAKey(key_value=(n, e))
        return RSAPairKeys(pub, priv)
