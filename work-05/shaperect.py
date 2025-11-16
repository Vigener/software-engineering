# 左下が(1.0, 1.0)でサイズが5.0×3.0の長方形を，xについては[0.0, 8.0]の範囲で0.25ごと，yについては[0.0, 5.0]の範囲で0.5ごとで描画することを表すクラスShapeRect．

from shape import Shape
from xyrange import XYRange
class ShapeRect(Shape):
    # 左下が(1.0, 1.0)でサイズが5.0×3.0の長方形
    def inside(self, x: float, y: float) -> bool:
        return 1.0 <= x and x <= 6.0 and 1.0 <= y and y <= 4.0

    # 描画範囲は，xが[0.0, 8.0]，0.25刻み．yが[0.0, 5.0]，0.5刻み．
    def get_range(self) -> XYRange:
        return XYRange(0.0, 8.0, 0.25, 0.0, 5.0, 0.5)