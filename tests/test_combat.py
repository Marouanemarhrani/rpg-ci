import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from character import Character
from combat import Combat

def test_combat_basic():
    a = Character()
    b = Character()
    fight = Combat(a, b)

    while not fight.is_over():
        fight.next_turn()

    assert fight.is_over()
    assert fight.winner() is not None
    assert fight.winner().is_dead() is False
