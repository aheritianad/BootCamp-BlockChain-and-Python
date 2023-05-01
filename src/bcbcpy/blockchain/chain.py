from bcbcpy import __author__


from bcbcpy.blockchain.block import Block, InitialBlock
from bcbcpy.utils import obj2txt


__all__ = ["Chain", "RootChain"]


class BaseChain:
    def __repr__(self):
        content = {"hash": self.hash, "data": self.data}
        return obj2txt(content)

    @property
    def hash(self):
        return self.last_block.hash

    @property
    def data(self):
        return self.last_block.data

    def add_block(self, block: Block):
        assert (
            self.last_block is block.prev_block
        ), "Incompatible block to the head block of the chain."
        assert block.is_valid(), "Block is not valid."
        self.last_block = block


class RootChain(BaseChain):
    def __init__(self, initial_data: str = "", difficulty: int = 4):
        super().__init__()
        self.root_block = InitialBlock(initial_data, difficulty)
        self.last_block = self.root_block


class Chain(BaseChain):
    def __init__(self, root_chain: BaseChain, info: str = "", difficulty: int = 4):
        self.root_block = Block(
            data=info, prev_block=root_chain.last_block, next_difficulty=difficulty
        )
        self.root_block.mine()
        self.last_block = self.root_block
