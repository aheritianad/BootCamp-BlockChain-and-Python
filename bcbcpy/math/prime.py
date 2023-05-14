import math
import random

try:
    from typing import Optional
except ModuleNotFoundError:
    from typing_extensions import Optional
except ModuleNotFoundError:
    from beartype import Optional


def get_s_d(n: int) -> tuple[int, int]:
    """
    Find s and d such that n - 1 = d * 2^s and d odd.

    Args:
        n (int): odd number to decompose.

    Returns:
        tuple[int, int]: s and d
    """
    assert n % 2 == 1, "n needs to be odd"

    s = 0
    d = n - 1
    while not d & 1:
        s += 1
        d >>= 1

    return s, d


def is_prime(n: int) -> bool:
    """
    Improved Miller-Rabin deterministic for *small* bits

    see # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
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
        if y != 1:
            return False
    return True


def is_probably_prime(n: int, runs: int) -> bool:
    """Miller-Rabin"""
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
        if y != 1:
            return False
    return True


def generate_probably_prime(bit_size: int, runs: Optional[int] = None) -> int:
    assert bit_size > 0
    if runs is None:
        runs = bit_size // 4 + 1
    while True:
        n = random.randint(2 ** (bit_size - 1), 2**bit_size - 1)
        if is_probably_prime(n, runs):
            return n
