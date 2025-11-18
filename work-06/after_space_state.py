# after_space_state.py

from __future__ import annotations
from state import Context, State
from typing import Optional

class AfterSpaceState(State):
  # 変数_instanceはAfterSpaceState型のデータまたは「無し」
  _instance: Optional[AfterSpaceState] = None

  @classmethod
  def get_instance(cls) -> AfterSpaceState:
    if cls._instance is None:
      cls._instance = AfterSpaceState()
    return cls._instance

  def process_char(self, c: Context, ch: str) -> str:
    # 相互importによるエラーを避けるために，import文をメソッド内に書いている
    from other_state import OtherState
    if not ch.isspace():
      c.set_state(OtherState.get_instance())
    return ch