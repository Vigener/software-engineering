# filter_iterator.py

from typing import Iterator

class FilterIterator(Iterator[str]):
  AFTER_SPACE: int = 1
  OTHER: int = 2

  def __init__(self, original: Iterator[str]) -> None:
    super().__init__()
    self._original: Iterator[str] = original
    self._state: int = FilterIterator.AFTER_SPACE

  def set_state(self, new_state: int):
    self._state = new_state
 
  def __next__(self) -> str:
    # ここで_originalから1文字取得して，chに代入する
    ch = next(self._original)

    if self._state == FilterIterator.AFTER_SPACE:
      if not ch.isspace():
        self.set_state(FilterIterator.OTHER)
      return ch
    else:
      if ch.isspace():
        self.set_state(FilterIterator.AFTER_SPACE)
        return ch
      return '.'
if __name__ == "__main__":
  for ch in iter("The quick brown fox jumps over a lazy dull dog.\n"):
    print(ch, end="")
  for ch in FilterIterator(iter("The quick brown fox jumps over a lazy dull dog.\n")):
    print(ch, end="")