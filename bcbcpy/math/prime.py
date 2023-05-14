import math
import random
from typing import Optional

from .arithmetic import get_s_d


def is_prime(n: int) -> bool:
    """
    Return `True` if the decimal number `n` is prime, and `False` o.w.

    Improved Miller-Rabin deterministic for *small* bits number (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases).
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    if n < 2_047:
        base_witness = [2]
    elif n < 1_373_653:
        base_witness = [2, 3]
    elif n < 9_080_191:
        base_witness = [31, 73]
    elif n < 25_326_001:
        base_witness = [2, 3, 5]
    elif n < 3_215_031_751:
        base_witness = [2, 3, 5, 7]
    elif n < 4_759_123_141:
        base_witness = [2, 7, 61]
    elif n < 1_122_004_669_633:
        base_witness = [2, 13, 23, 1662803]
    elif n < 2_152_302_898_747:
        base_witness = [2, 3, 5, 7, 11]
    elif n < 2_152_302_898_747:
        base_witness = [2, 3, 5, 7, 11]
    elif n < 3_474_749_660_383:
        base_witness = [2, 3, 5, 7, 11, 13]
    elif n < 341_550_071_728_321:
        base_witness = [2, 3, 5, 7, 11, 13, 17]
    elif n < 3_825_123_056_546_413_051:
        base_witness = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n < 318_665_857_834_031_151_167_461:
        base_witness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n < 3_317_044_064_679_887_385_961_981:
        base_witness = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    else:
        import warnings

        warnings.warn("It is recommended to use probabilistic test.")
        base_witness = range(2, min(n - 2, int(2 * math.log(n) ** 2)))

    s, d = get_s_d(n)

    for a in base_witness:
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:  # type: ignore
            return False
    return True


def is_probably_prime(n: int, runs: int) -> bool:
    """
    Miller-Rabin
    ====

    Return `True` if `n` is probably prime with probability `4^-runs` and `False` when it is sure to not be.
    """
    if n < 2:
        return False
    elif n in (2, 3, 5):
        return True
    elif n % 2 == 0:
        return False

    s, d = get_s_d(n)

    for _ in range(runs):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:  # type: ignore
            return False
    return True


def generate_probably_prime(bit_size: int, runs: Optional[int] = None) -> int:
    """
    Return a number of `bit_size` bits which is probably prime with probability `4^-runs`. `runs` will be set to `bit_size//4 + 1` when its value is `None`.
    """
    assert bit_size > 0
    if runs is None:
        runs = bit_size // 4 + 1
    while True:
        n = random.randint(2 ** (bit_size - 1), 2**bit_size - 1)
        if is_probably_prime(n, runs):
            return n
