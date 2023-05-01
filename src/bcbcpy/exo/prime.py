from bcbcpy import __author__


from typing import Tuple


def generate_primes(
    n_bit: int, num_out: int = 1
) -> int | Tuple[int, ...]:  # TODO update base.crypto.rsa when this is moved from exo
    while True:
        # --- TO IMPLEMENT --
        p = ...
        q = ...
        # -------------------
        if is_prime(p) and is_prime(q):  # type:ignore
            break
    return p, q  # type:ignore


def is_prime(n: int):
    out = True
    # --- TO IMPLEMENT --
    ...
    # -------------------
    return out
