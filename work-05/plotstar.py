# 図形の内側は"★"，外側は"　" （全角の空白）で描き，yが1つ増えるごとに2行改行することを表すクラスPlotStar．

from plot import Plot
class PlotStar(Plot):
    def plot_inside(self) -> None:
        print("★", end="")

    def plot_outside(self) -> None:
        print("　", end="")  # 全角の空白

    def next_line(self) -> None:
        print()
        print() # 2行改行

if __name__ == "__main__":
    PlotStar().draw()