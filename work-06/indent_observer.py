from filesystem import Observer
from filesystem import Entry

class IndentObserver(Observer):
  # 深さに応じてインデントする
  def print_entries(self, depth: int, e: Entry) -> None:
    print('   ' * depth + e.get_name()) # 深さ * 3スペース
    for child in e.get_children():
      self.print_entries(depth + 1, child)

  def update(self, e: Entry) -> None:
    # (depth=0) から始める
    self.print_entries(0, e)