from bcbcpy import __author__

from enum import Enum

from hashlib import new

__all__ = ["hash_function", "hash_nonce_initializer", "is_valid_hash", "HashName"]


class HashName(Enum):
    blake2b = "blake2b"
    blake2s = "blake2s"
    md5 = "md5"
    sha1 = "sha1"
    sha224 = "sha224"
    sha256 = "sha256"
    sha384 = "sha384"
    sha3_224 = "sha3_224"
    sha3_256 = "sha3_256"
    sha3_384 = "sha3_384"
    sha3_512 = "sha3_512"
    sha512 = "sha512"
    shake_128 = "shake_128"
    shake_256 = "shake_256"


def hash_function(*data, nonce: int = 0, hash_name: HashName = HashName.sha256) -> str:
    u_string = "".join(map(str, [*data, nonce]))
    b_string = u_string.encode(encoding="utf-8")
    hash_object = new(name=hash_name.name, data=b_string)
    hashed_value = hash_object.hexdigest()
    return hashed_value


def is_valid_hash(hash_value: str, difficulty: int = 4) -> bool:
    output = True
    for i in range(difficulty):
        if hash_value[i] != "0":
            return False
    return output


def hash_nonce_initializer(
    *initial_data: str, difficulty: int = 4, hash_name: HashName = HashName.sha256
) -> tuple[str, int]:
    nonce = 0
    while not is_valid_hash(
        tmp_hash := hash_function(*initial_data, nonce=nonce, hash_name=hash_name),
        difficulty=difficulty,
    ):
        nonce += 1
    return tmp_hash, nonce
