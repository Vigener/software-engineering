# ファイル fibseq.py

# ここにFibSequenceクラスを定義する
class FibSequence:
    def __init__(self, num: int):
        self._num = num

    def __iter__(self):
        return FibIterator(self._num)

class FibIterator:
    def __init__(self, num: int):
        self._num = num
        self._i = 0
        self._j = 1

    def __next__(self):
        if self._num <= 0:
            raise StopIteration

        # _i と _j を使って次に返すフィボナッチ数の値を変数valに格納する
        
        # _i, _j, _numを更新する
        val = self._j
        self._i, self._j = self._j, self._i + self._j
        self._num -= 1

        return val

if __name__ == "__main__":
    for v in FibSequence(10):
        print(v)