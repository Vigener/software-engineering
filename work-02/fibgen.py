# ファイル fibgen.py

# ジェネレータを使ってFibSequenceと同じ動作を実現する
class FibGenerator:
    def __init__(self, num: int):
        self._num = num

    def __iter__(self):
        num = self._num
        i = 0
        j = 1
        
        while num > 0:
            val = j
            i, j = j, i + j
            num -= 1
            yield val

if __name__ == "__main__":
    for v in FibGenerator(10):
        print(v)
