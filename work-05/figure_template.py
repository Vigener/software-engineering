# ファイル figure_template.py
from abc import ABC, abstractmethod
from xyrange import XYRange

class FigureTemplate(ABC):
    # (x, y)が図形の内側または境界線上ならtrueを，そうでなければfalseを返す．
    @abstractmethod
    def _inside(self, x: float, y: float) -> bool:
        pass

    # xの動く範囲[x1, x2]と動く間隔xstep，
    # yの動く範囲[y1, y2]と動く間隔ystepの6つの数の組を返す．
    @abstractmethod
    def _get_range(self) -> XYRange:
        pass

    # 現在の座標に図形の内側を表す一文字を書いて，x座標を1つ右へ動かす．
    @abstractmethod
    def _plot_inside(self) -> None:
        pass

    # 現在の座標に図形の外側を表す一文字を書いて，x座標を1つ右へ動かす．
    @abstractmethod
    def _plot_outside(self) -> None:
        pass

    # y座標を1つ下へ動かし，x座標を左端に動かす．
    @abstractmethod
    def _next_line(self) -> None:
        pass

    # x座標: x1からx2までのxstep刻み，
    # y座標: y1からy2までのystep刻み，の各点について，
    # (x, y)が図形の内側かどうかに従って異なる文字を書く．
    def draw(self) -> None:
        r = self._get_range()
        y = r.y2
        while y >= r.y1: # yに関するループ
            x = r.x1
            while x <= r.x2: # xに関するループ
                if self._inside(x, y):
                    self._plot_inside()
                else:
                    self._plot_outside()
                x += r.xstep
            self._next_line()
            y -= r.ystep