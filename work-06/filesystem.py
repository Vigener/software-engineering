# filesystem.py

# クラス内で自分自身の型を参照するために必要
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List
from typing import Optional

class Entry(ABC): # ファイルとディレクトリの共通の親クラス
  def __init__(self, name: str) -> None:
    self._name = name

  def get_name(self) -> str:
    return self._name

  @abstractmethod
  def get_children(self) -> List[Entry]:
    pass

class File(Entry):
  def __init__(self, name: str) -> None:
    super().__init__(name) # 親クラスの__init__の呼び出し

  def get_children(self) -> List[Entry]:
    return []
  
# 追加 ----------------------------
class Observer(ABC):
  @abstractmethod
  def update(self, e) -> None:
    pass

class Subject(ABC):
  @abstractmethod
  def add_observer(self, o: Observer) -> None:
    pass

  @abstractmethod
  def notify_observers(self) -> None:
    pass
# ---------------------------------

class Directory(Entry, Subject):
  def __init__(self, name: str) -> None:
    super().__init__(name) # 親クラスの__init__の呼び出し
    # 子要素を保存するリスト（Directory の内容）
    self._children: List[Entry] = []
    # 1. このディレクトリを観察する Observer を格納するリスト
    self._observers: List[Observer] = []

  def get_children(self) -> List[Entry]:
    return self._children

  def add(self, e: Entry) -> None:
    self._children.append(e)
    # 4. 子が追加されたら、登録された観察者に通知する
    self.notify_observers()

  def add_observer(self, o: Observer) -> None:
    # 2. 「観察者」を受け取り、それを「観察者リスト」に追加する
    self._observers.append(o)

  def notify_observers(self) -> None:
    # 3. 「観察者リスト」に登録されている全ての「観察者」のupdateメソッドを呼び出し、「自分が変化したこと」を
    for observer in self._observers:
      observer.update(self)

# ファイルシステム一般のインタフェースを与える．
class FileSystem(ABC):
  # 変数_instanceはFileSystem型のデータまたは「無し」
  _instance: Optional[FileSystem] = None

  @staticmethod
  def get_instance():
    # 唯一のインスタンスを（必要なら生成して）返す
    if (FileSystem._instance is None):
      FileSystem._instance = _SimpleFileSystem()
    return FileSystem._instance

  @abstractmethod
  def create_directory(self, name: str) -> Directory:
    pass

  @abstractmethod
  def create_file(self, name: str) -> File:
    pass

# 単純なファイルシステムの実装を与える．
class _SimpleFileSystem(FileSystem):
  def create_directory(self, name: str) -> Directory:
    return Directory(name)

  def create_file(self, name: str) -> File:
    return File(name)