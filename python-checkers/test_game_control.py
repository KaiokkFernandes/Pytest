import pytest
from game_control import GameControl

def test_get_turn():
    gc = GameControl("W", False)
    assert gc.get_turn() == "W"

def test_get_winner():
    gc = GameControl("W", False)
    # Inicialmente sem vencedor
    assert gc.get_winner() is None
