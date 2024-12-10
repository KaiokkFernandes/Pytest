import pytest
from piece import Piece
from unittest.mock import Mock

def test_get_name():
    p = Piece("0BN")
    assert p.get_name() == "0BN"

def test_get_position():
    p = Piece("10WN")
    assert p.get_position() == "10"

def test_get_color():
    p = Piece("0BN")
    assert p.get_color() == "B"

def test_get_has_eaten():
    p = Piece("0BN")
    p.set_has_eaten(True)
    assert p.get_has_eaten() is True

def test_is_king():
    p = Piece("0BY")
    assert p.is_king() is True
    p2 = Piece("0BN")
    assert p2.is_king() is False

def test_get_adjacent_squares():
    p = Piece("0WN")
    board_mock = Mock()
    board_mock.get_col_number.return_value = 0
    board_mock.get_row_number.return_value = 0
    board_mock.get_color_up.return_value = "W"
    adj = p.get_adjacent_squares(board_mock)
    assert isinstance(adj, list)

