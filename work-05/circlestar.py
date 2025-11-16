# FigureTemplateを継承したクラスCircleStar
# このクラスは以下の動作を提供するようにしなさい．
# - 中心(0.0, 0.0)，半径4.0の円を描く．
# - 描画範囲はxが[-5.0, 5.0]でyが[-5.0, 5.0]とする．文字を表示するのはxについては0.25ごとで，yについては0.5ごととする．
# - 円の内側には"★"，円の外側には".." （半角のピリオド2つ）を書く．
# - yが1つ増えるごとに2行改行する．

# circlestar.pyの末尾ではrectdot.pyと同様に，__name__が__main__である場合にCircleStar().draw()を呼び出すようにしなさい．

from figure_template import FigureTemplate
from xyrange import XYRange

class CircleStar(FigureTemplate):
    # 中心(0.0, 0.0)，半径4.0の円
    def _inside(self, x: float, y: float) -> bool:
        return x**2 + y**2 <= 4.0**2

    # 描画範囲は，xが[-5.0, 5.0]，0.25刻み．yが[-5.0, 5.0]，0.5刻み．
    def _get_range(self) -> XYRange:
        return XYRange(-5.0, 5.0, 0.25, -5.0, 5.0, 0.5)

    # # 内側なら"★"，外側なら".."
    def _plot_inside(self):
        print("★", end="")

    def _plot_outside(self):
        print("..", end="")
    #（動作確認用）→OK
    # def _plot_inside(self):
    #     print("*", end="")
    # def _plot_outside(self):
    #     print("_", end="")

    def _next_line(self):
        print()
        print()  # 2行改行

if __name__ == "__main__":
    CircleStar().draw()