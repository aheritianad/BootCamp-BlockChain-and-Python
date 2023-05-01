from bcbcpy import __author__


from bcbcpy.blockchain.block.block import Block
from bcbcpy.blockchain.block.transaction import TransactionBlock, TransactionData
from bcbcpy.node import Node as _Node

__all__ = ["Node"]


class Node(_Node):
    def make_transaction_data(
        self,
        assets: float,
        to: "Node",
        prev_block: Block,
        transaction_message: str = "",
    ):
        trans_data = TransactionData(
            assets, self, to.id, to.pub, prev_block, transaction_message
        )
        return trans_data

    def make_transaction_data(
        self,
        assets: float,
        to: "Node",
        prev_block: Block,
        transaction_message: str = "",
        next_difficulty: int = 4,
    ):
        trans_data = self.make_transaction_data(
            assets, to, prev_block, transaction_message
        )
        trans_block = TransactionBlock(trans_data, next_difficulty)
        return trans_block
