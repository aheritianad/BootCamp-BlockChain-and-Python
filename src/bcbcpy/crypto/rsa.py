from bcbcpy import __author__


from bcbcpy.crypto import Key, AsymmetricKeys
from bcbcpy.functional.math import (
    is_invertible_mod,
    int2base,
    base2int,
    generate_probably_prime,
)
from bcbcpy.utils import TOTAL_CHAR, txt2int, int2txt, obj2txt, txt2obj


from typing import Tuple
import random

__all__ = [
    "RSAKey",
    "RSAPairKeys",
    "rsa_convert",
    "read_from_rsa",
]


rsa_chunk_open_tag = "<rsachunkrsa>"
rsa_chunk_close_tag = "</rsachunkrsa>"
end_open_tag = len(rsa_chunk_open_tag)
begin_close_tag = len(rsa_chunk_close_tag)
remove_tags = lambda inp_txt: inp_txt[end_open_tag:-begin_close_tag]


def read_from_rsa(text: str):
    chunks = txt2obj(text)
    chunks = list(map(remove_tags, chunks))
    return "".join(chunks)


def rsa_convert(txt: str, key_value: Tuple[int, int], chunk_size: int = 2000):
    n, e = key_value
    assert n > TOTAL_CHAR, "Key too small."

    if rsa_chunk_open_tag in txt and rsa_chunk_close_tag in txt:
        chunks = txt2obj(txt)
        chunks = list(map(remove_tags, chunks))

    else:
        # consider it as raw
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
        out.append(rsa_chunk_open_tag + text + rsa_chunk_close_tag)
    return obj2txt(out, indent=0)


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
    def generate_pairs(n_bit: int | None = None, chunk_size: int = 2000):
        p = generate_probably_prime(n_bit // 2 + 1)
        q = generate_probably_prime(n_bit // 2 - 1)
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
