from bcbcpy import __author__


from bcbcpy.blockchain.block.block import Block, InitialBlock
from bcbcpy.utils import obj2txt


__all__ = ["Chain", "RootChain"]


class BaseChain:
    def __init__(self) -> None:
        self._length = 0
        self.root_block = self.last_block = None

    def __len__(self):
        return self._length

    def __repr__(self):
        root = {
            "hash": self.root_block.hash,
            "data": self.root_block.data[:15]
            + ("..." if len(self.root_block.data) > 15 else ""),
        }
        last = {
            "hash": self.last_block.hash,
            "data": self.last_block.data[:15]
            + ("..." if len(self.last_block.data) > 15 else ""),
        }
        content = {"root_block": root}

        if self._length > 1:
            if self._length > 2:
                content |= {"...": "..."}
            content |= {"last_block": last}
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
        self._length += 1

    def __iter__(self):
        current_block = self.last_block
        while current_block:
            yield current_block
            current_block = current_block.prev_block


class RootChain(BaseChain):
    def __init__(self, initial_data: str = "", difficulty: int = 4):
        super().__init__()
        self._length = 1
        self.root_block = self.last_block = InitialBlock(initial_data, difficulty)


class Chain(BaseChain):
    def __init__(self, root_chain: BaseChain, info: str = "", difficulty: int = 4):
        super().__init__()
        self._length = 1
        self.root_block = Block(
            data=info, prev_block=root_chain.last_block, next_difficulty=difficulty
        )
        self.root_block.mine()
        self.last_block = self.root_block
