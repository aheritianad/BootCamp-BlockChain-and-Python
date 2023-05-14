from bcbcpy.__ import __author__


from typing import List, Union

__all__ = ["get_s_d", "extended_gcd", "inverse_mod", "int2base", "base2int", "digits"]


def get_s_d(n: int) -> tuple[int, int]:
    """
    Find `(s,d)` such that `n - 1 = d * 2^s` and `d` odd for an odd number `n`.
    """
    assert n % 2 == 1, "n needs to be odd"

    s = 0
    d = n - 1
    while not d & 1:
        s += 1
        d >>= 1

    return s, d


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Return `(r, u, v)` where ``gcd(a,b) = r = a*u + b*v.
    """
    _u, u_ = 1, 0
    _v, v_ = 0, 1
    _r, r_ = a, b
    while r_ != 0:
        _r, (q, r_) = r_, divmod(_r, r_)
        _u, u_ = (u_, _u - q * u_)
        _v, v_ = (v_, _v - q * v_)
    return _r, _u, _v


def inverse_mod(a: int, n: int) -> Union[int, None]:
    """
    Return the inverse of `a mod n` or `None` if it is not invertible.
    """
    gcd, u, _ = extended_gcd(a, n)
    if gcd != 1:
        inverse = None
    else:
        inverse = u % n
    return inverse


def int2base(n: int, b: int) -> List[int]:
    """
    Return the list of digits of decimal `n` in base `b`.
    """
    assert b > 1 and isinstance(b, int) and isinstance(n, int)
    out = []
    while True:
        n, r = divmod(n, b)
        out.insert(0, r)
        if n == 0:
            break
    return out


def base2int(ns: List[int], b: int) -> int:
    """
    Return the decimal representation of the number in base `b` defined by its digits in `ns`.
    """
    assert b > 1 and isinstance(b, int)
    out = 0
    for n in ns:
        out *= b
        out += n
    return out


def digits(n: int, b: int = 10) -> list[int]:
    """
    Return the digits of a decimal `n` in base `b`.
    """

    if b == 10:
        out = [int(d) for d in str(n)]
    else:
        out = int2base(n, b)
    return out
