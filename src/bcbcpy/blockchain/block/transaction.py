from bcbcpy import __author__


from bcbcpy.blockchain.block import BaseBlock, Block
from bcbcpy.node import Node
from bcbcpy.crypto import Key
from bcbcpy.utils import obj2txt


from datetime import datetime

__all__ = ["TransactionData", "TransactionBlock"]


class TransactionData:
    def __init__(
        self,
        assets: float,
        sender: Node,
        receiver_id: str,
        receiver_pub: Key,
        prev_block: BaseBlock,
        transaction_message: str = "",
    ):
        self.prev_block = prev_block
        self.__make_data_dict(
            assets,
            sender,
            receiver_id,
            receiver_pub,
            prev_block.hash,
            transaction_message,
        )

    def __make_data_dict(
        self,
        assets: float,
        sender: Node,
        receiver_id: str,
        receiver_pub: Key,
        prev_hash,
        transaction_message: str,
    ):
        self.data_dict = {
            "timestamp": datetime.now().isoformat(),
            "sender_id": sender.id,
            "receiver_id": receiver_id,
            "assets": assets,
            "prev_hash": prev_hash,
            "sender_confirmation": self.__sender_signature(
                sender, assets, receiver_pub, prev_hash, transaction_message
            ),
        }

    def __getitem__(self, key: str):
        if key == "prev_block":
            return self.prev_block

        if key not in self.data_dict:
            raise KeyError(
                f"Key {key} is not a valid key for {self.__class__.__name__}."
            )
        return self.data_dict[key]

    def __sender_signature(
        self,
        sender: Node,
        assets: float,
        receiver_pub: Key,
        prev_hash: str,
        transaction_message: str,
    ):
        dict_contract = {
            "prev_hash": prev_hash,
            "value": assets,
            "receiver_pub_key_value": receiver_pub.key_value,
            "transaction message": sender.encrypt(
                message=transaction_message, key=receiver_pub
            ),
        }

        string_contract = obj2txt(
            dict_contract,
        )

        return sender.sign(string_contract)

    @property
    def data(self):
        return obj2txt(self.data_dict)

    def __repr__(self):
        return self.data


class TransactionBlock(Block):
    def __init__(self, transaction_data: TransactionData, next_difficulty: int = 4):
        super().__init__(
            data=transaction_data.data,
            prev_block=transaction_data["prev_block"],
            next_difficulty=next_difficulty,
        )
