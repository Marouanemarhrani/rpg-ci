class Character:
    def __init__(self, name=""):
        self.name = name
        self.hp = 10

    def is_dead(self):
        return self.hp <= 0

    def attack(self, other):
        other.hp -= 1

    def heal(self):
        if self.hp < 10:
            self.hp += 1
