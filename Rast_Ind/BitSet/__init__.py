from typing import List, Iterator


class BitSet:
    def __init__(self, ) -> None:
        self._bit_permission: list = list()



    def __str__(self) -> str:
        return ''.join(map(str, self._bit_permission))

    def __getitem__(self, index:int) -> int:
        return self._bit_permission[index]

    def __setitem__(self, index:int, value) -> None:
        self._bit_permission[index] = value

    def __len__(self) -> int:
        return len(self._bit_permission)

    def __iter__(self) -> Iterator[int]:
        return iter(self._bit_permission)
