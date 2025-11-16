# ファイル strategy_test.py
import sys

from xyrange import XYRange
from shape import Shape
from shaperect import ShapeRect
from shapecircle import ShapeCircle
from plot import Plot
from plotdot import PlotDot
from plotstar import PlotStar

def error():
    print("Usage: python3 strategy_test.py [rect or circle] [dot or star]")
    exit(1)

# x座標: x1からx2までxstep刻み
# y座標: y1からy2までystep刻み，の各点について，
# (x, y)が図形の内側かどうかに従って文字を書く．

def draw(shape: Shape, plot: Plot) -> None:
    r: XYRange = shape.get_range()
    y = r.y2
    while y >= r.y1: # yに関するループ
        x = r.x1
        while x <= r.x2: # xに関するループ
            if shape.inside(x, y):
                plot.plot_inside()
            else:
                plot.plot_outside()
            x += r.xstep
        plot.next_line()
        y -= r.ystep

args = sys.argv[1:]
if (len(args) != 2):
    error()

shape: Shape
if args[0] == "rect":
    shape = ShapeRect()
elif args[0] == "circle":
    shape = ShapeCircle()
else:
    error()

plot: Plot
if args[1] == "star":
    plot = PlotStar()
elif args[1] == "dot":
    plot = PlotDot()
else:
    error()

draw(shape, plot)