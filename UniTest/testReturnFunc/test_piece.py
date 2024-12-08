import pytest
from unittest.mock import Mock

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../python-checkers')))

from piece import Piece


@pytest.fixture
def mock_board():
    board = Mock()
    board.get_col_number.side_effect = lambda pos: int(str(pos)[1])
    board.get_row_number.side_effect = lambda pos: int(str(pos)[0])
    board.get_color_up.return_value = "W"  # Assume que a cor "W" é para cima
    board.has_piece.return_value = False
    board.get_pieces_by_coords.side_effect = lambda *coords: [None] * len(coords)
    return board


def test_get_position():
    piece = Piece("20WN")
    assert piece.get_position() == "20"


def test_get_color():
    piece = Piece("20WN")
    assert piece.get_color() == "W"


def test_is_king():
    piece = Piece("20WN")
    assert not piece.is_king()
    piece.set_is_king(True)
    assert piece.is_king()


def test_set_position():
    piece = Piece("20WN")
    piece.set_position(30)
    assert piece.get_position() == "30"


def test_get_adjacent_squares(mock_board):
    mock_board.get_col_number.side_effect = lambda pos: pos % 10
    mock_board.get_row_number.side_effect = lambda pos: pos // 10
    piece = Piece("20WN")
    adjacent_squares = piece.get_adjacent_squares(mock_board)
    assert len(adjacent_squares) == 2  # Ajustar este valor com base na lógica esperada





def test_get_moves_empty_board(mock_board):
    mock_board.get_pieces_by_coords.side_effect = lambda *coords: [None] * len(coords)
    mock_board.get_col_number.side_effect = lambda pos: pos % 10
    mock_board.get_row_number.side_effect = lambda pos: pos // 10
    piece = Piece("20WN")
    moves = piece.get_moves(mock_board)
    assert len(moves) == 2  # Ou ajuste para o valor esperado real






def test_get_moves_with_eating(mock_board):
    piece = Piece("20WN")
    mock_board.get_pieces_by_coords.side_effect = lambda *coords: [
    Mock(get_color=lambda: "B", get_position=lambda: "31"),
    None,
    ]
    mock_board.has_piece.side_effect = lambda pos: pos != 42  # Somente posição 42 está livre
    mock_board.get_col_number.side_effect = lambda pos: pos % 10
    mock_board.get_row_number.side_effect = lambda pos: pos // 10

    piece = Piece("20WN")
    moves = piece.get_moves(mock_board)
    assert len(moves) == 1  # Ajuste para capturas reais

