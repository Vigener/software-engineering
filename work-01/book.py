class Book:
    # オブジェクト生成時に _author フィールドと _title フィールドをセットする．
    def __init__(self, author, title):
        self._author = author
        self._title = title
        # 3. _pagesの定義
        self._pages = 0
    
    # --- 1. プロパティの追加
    @property
    def author(self):
        return self._author
    
    @property
    def title(self):
        return self._title
    
    # 3. _pagesのプロパティ
    @property
    def pages(self):
        return self._pages
    
    # 5. プロパティを代入可能にする。
    @pages.setter
    def pages(self, p):
        self._pages = p
    
    # 2. インスタンスメソッド
    def print_author(self):
        print(self._author)
    
    def print_title(self):
        print(self._title)
    # --------------------------------------
    
    # 3. _pagesの表示メソッド
    def print_pages(self):
        print(self._pages)
        
    # 4. print_details
    def print_details(self):
        self.print_author()
        self.print_title()
        self.print_pages()

if __name__ == "__main__": # このファイルをimportではなく実行したときに真になる
    b1 = Book("Charles Dickens", "A Christmas Carol")
    b1.pages = 92
    b1.print_details()
    b2 = Book("Osamu Dazai", "No Longer Human")
    b2.pages = 154
    b2.print_details()