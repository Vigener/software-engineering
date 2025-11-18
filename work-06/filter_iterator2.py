# filter_iterator2.py

from typing import Iterator

from state import State
from state import Context
from after_space_state import AfterSpaceState

class FilterIterator2(Iterator[str], Context):
  def __init__(self, original: Iterator[str]) -> None:
    super().__init__()
    self._original: Iterator[str] = original
    self._state: State = AfterSpaceState.get_instance()

  def set_state(...) -> None:
    ...

  def __next__(self) -> str:
    # ここで_originalから1文字取得して，chに代入する
    ...

if __name__ == "__main__":
  for ch in iter("The quick brown fox jumps over a lazy dull dog.\n"):
    print(ch, end="")
  for ch in FilterIterator2(iter("The quick brown fox jumps over a lazy dull dog.\n")):
    print(ch, end="")