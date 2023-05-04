from bcbcpy import __author__


from bcbcpy.blockchain.block import Block
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
        prev_block: Block,
    ):
        self.prev_block = prev_block
        self.__make_data_dict(
            assets,
            sender,
            receiver_id,
            receiver_pub,
            prev_block.hash,
        )

    def __make_data_dict(
        self,
        assets: float,
        sender: Node,
        receiver_id: str,
        receiver_pub: Key,
        prev_hash,
    ):
        self.data_dict = {
            "timestamp": datetime.now().isoformat(),
            "sender_id": sender.id,
            "receiver_id": receiver_id,
            "assets": assets,
            "prev_hash": prev_hash,
            "sender_confirmation": sender.sign(
                f"[['assets',\t{assets}],\n['receiver_pub',\t{receiver_pub}],\n['prev_hash',\t{prev_hash}]]"
            ),
        }

    @property
    def data(self):
        return str(self.data_dict)

    def __repr__(self):
        return self.data

    def __getitem__(self, key: str):
        if key == "prev_block":
            return self.prev_block

        if key not in self.data_dict:
            raise KeyError(
                f"Key {key} is not a valid key for {self.__class__.__name__}."
            )
        return self.data_dict[key]


class TransactionBlock(Block):
    def __init__(
        self, transaction_data: TransactionData, next_difficulty: int | None = None
    ):
        super().__init__(
            data=transaction_data.data,
            prev_block=transaction_data["prev_block"],
            next_difficulty=next_difficulty,
        )
