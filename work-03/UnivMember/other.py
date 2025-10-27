class Other:
    # インスタンス変数として文字列 _name と整数 _age を保持し、それらの初期値はオブジェクトの引数で与えられる。
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def greet(self):
            print(f"I am a university member.")
            print(f"I am {self._name}.")
            print(f"I am {self._age} years old.")