from bcbcpy import __author__


from typing import List

__all__ = ["extended_gcd", "is_invertible_mod", "int2base", "base2int", "digits"]


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    extended_gcd(a,b) = (r,u, v) with gcd(a,b) = r = a*u + b*v
    """
    _u, u_ = 1, 0
    _v, v_ = 0, 1
    _r, r_ = a, b
    while r_ != 0:
        _r, (q, r_) = r_, divmod(_r, r_)
        _u, u_ = (u_, _u - q * u_)
        _v, v_ = (v_, _v - q * v_)
    return _r, _u, _v


def is_invertible_mod(a: int, n: int) -> tuple[bool, int]:
    gcd, inverse, _ = extended_gcd(a, n)
    return gcd == 1, inverse % n


def int2base(n: int, b: int) -> List[int]:
    assert b > 1 and isinstance(b, int) and isinstance(n, int)
    out = []
    while True:
        n, r = divmod(n, b)
        out.insert(0, r)
        if n == 0:
            break
    return out


def base2int(ns: List[int], b: int) -> int:
    assert b > 1 and isinstance(b, int)
    out = 0
    for n in ns:
        out *= b
        out += n
    return out


def digits(n: int, b: int = 10) -> list[int]:
    if b == 10:
        out = [int(d) for d in str(n)]
    else:
        out = int2base(n, b)
    return out
