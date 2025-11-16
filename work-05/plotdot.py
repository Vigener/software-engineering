# 図形の内側は"*"，外側は"_"で描き，yが1つ増えるごとに1行改行することを表すクラスPlotDot．

from plot import Plot
class PlotDot(Plot):
    def plot_inside(self) -> None:
        print("*", end="")

    def plot_outside(self) -> None:
        print("_", end="")

    def next_line(self) -> None:
        print()

if __name__ == "__main__":
    PlotDot().draw()