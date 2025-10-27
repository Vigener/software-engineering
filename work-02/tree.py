# ファイル tree.py
from __future__ import annotations
from typing import Iterable, Iterator, List, Optional

class Tree(Iterable['Tree']):
    def __init__(self, label: str, left: Optional[Tree], right: Optional[Tree]) -> None:
        self._label = label
        self._left = left
        self._right = right

    def __iter__(self) -> Iterator[Tree]:
        return _TreeIterator(self)

class _TreeIterator(Iterator[Tree]):
    def __init__(self, tree: Tree) -> None:
        self._stack = []
        self._stack.append(tree)  # 木の根だけをスタックにpushしておく．

    def __next__(self) -> Tree:
        if len(self._stack) == 0:
            raise StopIteration

        node = self._stack.pop()  # これから調べるノードをスタックからpopする．

        # そのノードに子供があれば，将来nextが呼ばれた時にそれらも調べられるよう
        # スタックにpushしておくコードをここに追記する．
        if node._right is not None:
            self._stack.append(node._right)
        if node._left is not None:
            self._stack.append(node._left)
        

        return node  # 最初にスタックからpopしたノードを返す．
