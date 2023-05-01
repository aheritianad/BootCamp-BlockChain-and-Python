from bcbcpy import __author__


from bcbcpy.crypto import Key, AsymmetricKeys
from bcbcpy.functional.math import is_invertible_mod, int2base, base2int
from bcbcpy.utils import TOTAL_CHAR, txt2int, int2txt, obj2txt, txt2obj


from bcbcpy.exo.prime import generate_primes  # TODO update when it is moved from exo


from typing import Tuple
import random

__all__ = [
    "RSAKey",
    "RSAPairKeys",
    "rsa_convert",
    "read_from_rsa_convert",
    "rsa_key_demo",
]


class RSAKey(Key):
    def __init__(self, key_value: Tuple[int, int], chunk_size: int = 2000):
        convert = lambda txt, key_value: rsa_convert(txt, key_value, chunk_size)
        super().__init__(
            key_value,
            convert,
        )


class RSAPairKeys(AsymmetricKeys):
    def __init__(self, pub: RSAKey, priv: RSAKey):
        super().__init__(pub, priv)

    def __repr__(self):
        return f"RSAPairKeys({self._first}, HIDDEN_KEY)"

    @staticmethod
    def generate_pairs(n_bit: int, chunk_size: int = 2000):
        p, q = generate_primes(n_bit, num_out=2)  # type:ignore
        n = p * q
        phi = (p - 1) * (q - 1)

        ds = list(range(phi // 4, 3 * phi // 4))
        random.shuffle(ds)

        for d in ds:
            stop, e = is_invertible_mod(d, phi)
            if stop:
                break
        else:
            d = e = phi - 1  # not supposed to happened, but I still put it for security

        pub = RSAKey(key_value=(n, d), chunk_size=chunk_size)
        priv = RSAKey(key_value=(n, e), chunk_size=chunk_size)
        return RSAPairKeys(pub, priv)


def rsa_convert(txt: str, key_value: Tuple[int, int], chunk_size: int = 2000):
    n, e = key_value
    assert n > TOTAL_CHAR, "Key too small."

    chunks = txt2obj(txt)

    if not isinstance(chunks, list) and any(
        not isinstance(chunk, str) for chunk in chunks
    ):
        chunks = txt  # ignore loading and consider it as txt

    if isinstance(chunks, str):
        chunks = [
            txt[i * chunk_size : (i + 1) * chunk_size]
            for i in range(len(txt) // chunk_size + 1)
        ]

    out = []
    for chunk in chunks:
        base_10 = txt2int(chunk)
        base_n = int2base(base_10, n)
        cip_n = [pow(digit, e, n) for digit in base_n]
        cip_10 = base2int(cip_n, n)
        text = int2txt(cip_10)
        out.append(text)
    return obj2txt(out, indent=0, separators=(",", ":"))


def read_from_rsa_convert(text: str):
    return "".join(txt2obj(text))


def rsa_key_demo(chunk_size: int = 2000):
    p = 103
    q = 71
    n = p * q
    d = 73
    e = 4597
    pub = RSAKey(key_value=(n, d), chunk_size=chunk_size)
    priv = RSAKey(key_value=(n, e), chunk_size=chunk_size)
    return RSAPairKeys(pub, priv)
