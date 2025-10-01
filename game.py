class Character:
    def __init__(self, name: str, hp: int):
        self._name = name
        self._hp = hp
        
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def print_status(self):
        print(f"Name:  {self._name}\nHP:   {self._hp}")

class Player(Character):
    def __init__(self, name: str, hp: int, experience: int):
        super().__init__(name, hp)
        # 自身の属性を初期化する
        self._experience = experience
    
    @property
    def experience(self):
        return self._experience
    
    def print_status(self): # オーバーライド
        super().print_status() # 親クラスのメソッドを呼び出せる
        print(f"Experience:   {self._experience}")
        
    def attack(self, enemy):
        print(f"{self._name} attacks {enemy.name}!")
        print(f"Experience: {self._experience} -> {self._experience + 1}")
        self._experience += 1
        
class Enemy(Character):
    def __init__(self, name: str, hp: int, evilness: int):
        super().__init__(name, hp)
        # 自身の属性を初期化する
        self._evilness = evilness
        
    @property
    def evilness(self):
        return self._evilness
    
    def print_status(self):
        super().print_status()
        print(f"Evilness:   {self._evilness}")
        
if __name__ == "__main__":
    p = Player("ITF", 100, 0)
    e = Enemy("Wizard", 30, 78)
    p.print_status()
    e.print_status()
    p.attack(e)
    p.attack(e)