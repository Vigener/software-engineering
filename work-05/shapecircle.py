# 中心が(0.0, 0.0)で半径3.0の円を，xについては[-5.0, 5.0]の範囲で0.25ごと，yについては[-5.0, 5.0]の範囲で0.5ごとで描画することを表すクラスShapeCircle．

from shape import Shape
from xyrange import XYRange
class ShapeCircle(Shape):
    # 中心(0.0, 0.0)，半径3.0の円
    def inside(self, x: float, y: float) -> bool:
        return x**2 + y**2 <= 3.0**2

    # 描画範囲は，xが[-5.0, 5.0]，0.25刻み．yが[-5.0, 5.0]，0.5刻み．
    def get_range(self) -> XYRange:
        return XYRange(-5.0, 5.0, 0.25, -5.0, 5.0, 0.5)