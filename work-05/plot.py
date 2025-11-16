# ファイル plot.py
from abc import ABC, abstractmethod
from xyrange import XYRange

class Plot(ABC):
    # 現在の座標に図形の内側を表す一文字を書いて，x座標を1つ右へ動かす．
    @abstractmethod
    def plot_inside(self) -> None:
        pass

    # 現在の座標に図形の外側を表す一文字を書いて，x座標を1つ右へ動かす．
    @abstractmethod
    def plot_outside(self) -> None:
        pass

    # y座標を1つ下へ動かし，x座標を左端に動かす．
    @abstractmethod
    def next_line(self) -> None:
        pass