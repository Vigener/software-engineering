class Book:
    # オブジェクト生成時に _author フィールドと _title フィールドをセットする．
    def __init__(self, author, title):
        self._author = author
        self._title = title
    # さらにメソッドを追加...
    