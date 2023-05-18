from bcbcpy.__ import __author__


from bcbcpy.crypto.basekey import BaseKey as Key, BasePairKeys as PairKeys
from bcbcpy.crypto.hash import hash_function
from bcbcpy.utils import add_noises, remove_noises


from typing import Optional


__all__ = ["Node"]


class Node:
    def __init__(self, keys: PairKeys, username: Optional[str] = None) -> None:
        """
        _summary_

        Args:
            keys (PairKeys): _description_
            username (Optional[str], optional): _description_. Defaults to None.
        """
        if username is None:
            username = "user"
        pub, _ = keys
        address = hash_function(pub)
        self.id = username + "_" + address[:2] + address[4::8]
        self.__keys = keys

    @property
    def pub(self) -> Key:
        return self.__keys.pub

    def encrypt(self, message: str, key: Key) -> str:
        return key.encode(message)

    def decrypt(self, cipher_text: str) -> str:
        return self.__keys.decrypt(cipher_text)

    def sign(self, message: str) -> str:
        return self.__keys.sign(message)

    def sends(
        self,
        message: str,
        _to: "Node|Key",
        _with_noises: bool = False,
    ) -> str:
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
    ) -> str:
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
        message = key.encode(signed_message)  # unsign

        if _with_noise:
            message = remove_noises(message)

        clear_message = message
        return clear_message
