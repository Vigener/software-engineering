# other_state.py

from __future__ import annotations
from state import Context, State
from typing import Optional

class OtherState(State):
  # 変数_instanceはOtherState型のデータまたは「無し」
  _instance: Optional[OtherState] = None

  @classmethod
  def get_instance(cls) -> OtherState:
    if cls._instance is None:
      cls._instance = OtherState()
    return cls._instance

  def process_char(self, c: Context, ch: str) -> str:
    # 相互importによるエラーを避けるために，import文をメソッド内に書いている
    from after_space_state import AfterSpaceState
    # 空白文字だったら状態を AfterSpaceState に戻す，空白文字自体はそのまま返す
    if ch.isspace():
      c.set_state(AfterSpaceState.get_instance())
      return ch
    # 空白以外の文字はドットにする
    return '.'