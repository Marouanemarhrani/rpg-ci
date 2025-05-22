class Combat:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.turn = 0

    def next_turn(self):
        if self.turn % 2 == 0:
            self.fighter1.attack(self.fighter2)
        else:
            self.fighter2.attack(self.fighter1)
        self.turn += 1

    def is_over(self):
        return self.fighter1.is_dead() or self.fighter2.is_dead()

    def winner(self):
        if self.fighter1.is_dead():
            return self.fighter2
        elif self.fighter2.is_dead():
            return self.fighter1
        return None
