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

  # ヒント2： FilterIterator2ではFilterIteratorと同じくset_stateが定義されるが，整数ではなくStateクラスのオブジェクトを状態として使用するので，FilterIteratorのset_stateとは引数の型が異なる．
  def set_state(self, new_state: State): # new_stateがintではなく、Stateクラスのオブジェクトになる
    self._state = new_state

  def __next__(self) -> str:
    # ここで_originalから1文字取得して，chに代入する
    # ヒント1： FilterIterator2の__next__メソッドは，Stateクラスのprocess_charメソッドを呼び出すような，ごく短いものになる．
    ch = next(self._original)
    return self._state.process_char(self, ch)

if __name__ == "__main__":
  for ch in iter("The quick brown fox jumps over a lazy dull dog.\n"):
    print(ch, end="")
  for ch in FilterIterator2(iter("The quick brown fox jumps over a lazy dull dog.\n")):
    print(ch, end="")