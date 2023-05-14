from bcbcpy.__ import __author__


from bcbcpy.crypto import hash_function, is_valid_hash
from bcbcpy.utils import obj2txt


__all__ = ["InitialBlock", "Block", "MultipleBlocks"]


class BaseBlock:
    def __init__(
        self,
        data: str = "",
        prev_block: "BaseBlock | None" = None,
        difficulty: int = 4,
        next_difficulty: int | None = None,
    ) -> None:
        self._nonce = 0
        self.data = data
        self.prev_block = prev_block
        self.difficulty = difficulty

        if next_difficulty is None:
            next_difficulty = difficulty

        self.next_difficulty = next_difficulty

    @property
    def prev_hash(self) -> str:
        if self.prev_block is None:
            return ""
        return self.prev_block.hash

    def __repr__(self) -> str:
        return obj2txt(
            {
                "prev_hash": self.prev_hash,
                "hash": self.hash,
                "data": self.data,
                "nonce": self.nonce,
            }
        )

    @property
    def nonce(self) -> int:
        return self._nonce

    @property
    def hash(self) -> str:
        return hash_function(self.data, self.prev_hash, nonce=self.nonce)

    def is_valid(self) -> bool:
        return is_valid_hash(self.hash, self.difficulty)

    def mine(self) -> None:
        self._nonce = 0
        while True:
            if self.is_valid():
                break
            self._nonce += 1


class InitialBlock(BaseBlock):
    def __init__(
        self,
        initial_data: str = "",
        difficulty: int = 4,
        next_difficulty: int | None = None,
    ) -> None:
        super().__init__(
            data=initial_data,
            prev_block=None,
            difficulty=difficulty,
            next_difficulty=next_difficulty,
        )
        self.mine()


class Block(BaseBlock):
    def __init__(
        self, data: str, prev_block: BaseBlock, next_difficulty: int | None = None
    ) -> None:
        super().__init__(data, prev_block, prev_block.next_difficulty, next_difficulty)


class MultipleBlocks(Block):
    def __init__(
        self,
        *blocks: Block,
    ) -> None:
        prev_block = blocks[0].prev_block
        for i, block in enumerate(blocks[1:]):
            assert (
                block.prev_block is prev_block
            ), f"Block number {i+2} has different previous block to its other predecessor blocks."

        self.blocks = blocks

        super().__init__(self.data, prev_block, self.next_difficulty)

    @property
    def data(self) -> str:
        return obj2txt(
            {
                "data": {
                    f"block {i+1}": block.data for i, block in enumerate(self.blocks)
                }
            },
        )

    @property
    def next_difficulty(self):
        return max(map(self._get_next_difficulty, self.blocks))

    def _get_next_difficulty(self, block: Block):
        return block.next_difficulty
