import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from character import Character

def test_character_initial_hp():
    c = Character()
    assert c.hp == 10

def test_character_death():
    c = Character()
    c.hp = 0
    assert c.is_dead() is True

def test_character_attack():
    a = Character()
    b = Character()
    a.attack(b)
    assert b.hp == 9

def test_character_heal():
    c = Character()
    c.hp = 5
    c.heal()
    assert c.hp == 6

def test_character_cannot_overheal():
    c = Character()
    c.hp = 10
    c.heal()
    assert c.hp == 10

def test_character_dies_after_multiple_attacks():
    attacker = Character()
    target = Character()

    for _ in range(10):
        attacker.attack(target)

    assert target.hp == 0
    assert target.is_dead()

def test_character_fight_until_death():
    attacker = Character()
    defender = Character()

    # Attaquer jusqu'à ce que le défenseur soit mort
    while not defender.is_dead():
        attacker.attack(defender)

    assert defender.hp <= 0
    assert defender.is_dead() is True

def test_combat_draw():
    a = Character()
    b = Character()
    
    a.hp = 1
    b.hp = 1

    class MutualCombat:
        def __init__(self, c1, c2):
            self.c1 = c1
            self.c2 = c2

        def run(self):
            self.c1.attack(self.c2)
            self.c2.attack(self.c1)

        def is_draw(self):
            return self.c1.is_dead() and self.c2.is_dead()

    fight = MutualCombat(a, b)
    fight.run()

    assert fight.is_draw() is True

def test_character_survives_with_heal_during_fight():
    c = Character()
    attacker = Character()

    # Le personnage subit 5 attaques
    for _ in range(5):
        attacker.attack(c)

    # Il se soigne 3 fois
    for _ in range(3):
        c.heal()

    # Il a reçu 5 dégâts (-5) puis +3 soins → hp = 8
    assert c.hp == 8
    assert c.is_dead() is False

def test_character_alternate_attack_and_heal():
    attacker = Character()
    defender = Character()

    # Le défenseur est attaqué 3 fois
    for _ in range(3):
        attacker.attack(defender)

    # Il se soigne 2 fois
    for _ in range(2):
        defender.heal()

    # Encore 2 attaques
    attacker.attack(defender)
    attacker.attack(defender)

    # Vérification : hp = 10 - 3 + 2 - 2 = 7
    assert defender.hp == 7
    assert defender.is_dead() is False
