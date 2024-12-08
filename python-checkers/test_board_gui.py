import pytest
from unittest.mock import Mock
from board_gui import BoardGUI
import pygame

@pytest.fixture
def mock_board():
    b = Mock()
    # Mock de peças retornando algo simplificado
    piece_mock = Mock()
    piece_mock.get_position.return_value = "0"
    piece_mock.get_color.return_value = "W"
    piece_mock.is_king.return_value = False
    b.get_pieces.return_value = [piece_mock]
    b.get_row_number.return_value = 0
    b.get_col_number.return_value = 0
    return b

def test_get_piece_properties(mock_board):
    gui = BoardGUI(mock_board)
    props = gui.get_piece_properties(mock_board)
    assert isinstance(props, list)
    assert "rect" in props[0]
    assert "color" in props[0]
    assert "is_king" in props[0]

def test_get_piece_by_index(mock_board):
    gui = BoardGUI(mock_board)
    piece = gui.get_piece_by_index(0)
    assert isinstance(piece, dict)

def test_show_piece(mock_board):
    gui = BoardGUI(mock_board)
    gui.hidden_piece = 2
    shown = gui.show_piece()
    assert shown == 2
    assert gui.hidden_piece == -1

def test_get_piece_on_mouse(mock_board):
    gui = BoardGUI(mock_board)
    result = gui.get_piece_on_mouse((50, 50))
    assert result is None or isinstance(result, dict)

def test_get_move_marks(mock_board):
    gui = BoardGUI(mock_board)
    assert isinstance(gui.get_move_marks(), list)

