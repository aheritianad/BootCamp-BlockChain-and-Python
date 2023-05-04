from bcbcpy import __author__


from bcbcpy.crypto import Key, BaseKeys, RSAKey, read_from_rsa
from bcbcpy.utils import add_noises, remove_noises


from typing import Optional
import random


__all__ = ["Node"]


class Node:
    def __init__(self, keys: BaseKeys, username: Optional[str] = None):
        if username is None:
            username = f"user_{random.random()*1e6:.0f}"
        self.id = username
        self.__keys = keys

    @property
    def pub(self):
        return self.__keys.pub

    def encrypt(self, message: str, key: Key):
        return key.convert(message)

    def decrypt(self, cipher_text: str):
        return self.__keys.decrypt(cipher_text)

    def sign(self, message: str):
        return self.__keys.sign(message)

    def sends(
        self,
        message: str,
        _to: "Node|Key",
        _with_noises: bool = False,
    ):
        if isinstance(_to, Key):
            key = _to
        elif isinstance(_to, Node):
            key = _to.pub
        else:
            raise TypeError("_to needs to be either Node or Key type.")

        if _with_noises:
            message = add_noises(message)

        signed_message = self.sign(message)
        cipher_text = self.encrypt(signed_message, key)

        if _with_noises:
            cipher_text = "NoIsYnOiSy" + cipher_text + "NoIsYnOiSy"

        return cipher_text

    def gets(
        self,
        message: str,
        _from: "Node|Key",
    ):
        if isinstance(_from, Key):
            key = _from
        elif isinstance(_from, Node):
            key = _from.pub
        else:
            raise TypeError("_from needs to be either Node or Key type.")

        _with_noise = False
        if message.startswith("NoIsYnOiSy") and message.endswith("NoIsYnOiSy"):
            message = message[10:-10]  # trim NoIsYnOiSy from head and tail
            _with_noise = True

        signed_message = self.decrypt(message)
        message = key.convert(signed_message)  # unsign

        if isinstance(key, RSAKey):
            message = read_from_rsa(message)

        if _with_noise:
            message = remove_noises(message)

        clear_message = message
        return clear_message
