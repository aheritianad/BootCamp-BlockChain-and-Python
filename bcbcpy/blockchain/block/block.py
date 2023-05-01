from bcbcpy import __author__


from bcbcpy.crypto import hash_nonce_initializer, hash_function, is_valid_hash
from bcbcpy.utils import obj2txt


__all__ = ["InitialBlock", "BaseBlock", "Block", "MultipleBlocks"]


class BaseBlock:
    def __init__(self, data: str = "", difficulty: int = 4, init: bool = True):
        if init:
            self.prev_hash = ""
            self.data = data
            self._hash, self._nonce = hash_nonce_initializer(
                data, difficulty=difficulty
            )
            self.next_difficulty = difficulty

    def __repr__(self):
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
        return self._hash

    def is_valid(self):
        raise NotImplementedError

    def _get_hash_for_a_given_nonce(self, nonce: int):
        self._hash = hash_function(self.prev_hash, self.data, nonce=nonce)
        return self._hash

    def __str__(self):
        return obj2txt({"data": self.data, "hash": self.hash})


class InitialBlock(BaseBlock):
    def __init__(self, initial_data: str = "", difficulty: int = 4):
        super().__init__(initial_data, difficulty, True)

    def is_valid(self):
        return True


class Block(BaseBlock):
    def __init__(self, data: str, prev_block: BaseBlock, next_difficulty: int = 4):
        super().__init__(init=False)
        assert prev_block.is_valid(), "Previous Block must be a valid block."
        self.data = data
        self.prev_block = prev_block
        self.next_difficulty = next_difficulty
        self._nonce = 0
        self._hash = self._get_hash_for_a_given_nonce(self._nonce)

    @property
    def prev_hash(self):
        return self.prev_block.hash

    def is_valid(self):
        return is_valid_hash(
            hash_value=self._get_hash_for_a_given_nonce(self.nonce),
            difficulty=self.prev_block.next_difficulty,
        )

    def mine(self):
        self._nonce = 0
        while True:
            if self.is_valid():
                break
            self._nonce += 1
        return self._hash


class MultipleBlocks(Block):
    def __init__(
        self,
        *blocks: Block,
    ):
        prev_block = blocks[0].prev_block
        for i, block in enumerate(blocks[1:]):
            assert (
                block.prev_block is prev_block
            ), f"Block number {i+2} has different previous block to its other predecessor blocks."

        data = obj2txt(
            {"data": {f"block {i+1}": [block.data] for i, block in enumerate(blocks)}},
        )

        next_difficulty = max(map(self._get_next_difficulty, blocks))

        super().__init__(data, prev_block, next_difficulty)

    def _get_next_difficulty(self, block: Block):
        return block.next_difficulty
