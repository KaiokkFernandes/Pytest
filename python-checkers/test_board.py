import pytest
from board import Board
from piece import Piece

@pytest.fixture
def mock_pieces():
    # Cria algumas peças falsas
    return [Piece("0BN"), Piece("1WN"), Piece("2BN"), Piece("3WN")]

def test_get_color_up():
    board = Board([], "W")
    assert board.get_color_up() == "W"

def test_get_pieces(mock_pieces):
    board = Board(mock_pieces, "B")
    p = board.get_pieces()
    assert len(p) == 4
    assert all(isinstance(x, Piece) for x in p)

def test_get_piece_by_index(mock_pieces):
    board = Board(mock_pieces, "B")
    piece = board.get_piece_by_index(0)
    assert piece.get_position() == "0"

def test_has_piece(mock_pieces):
    board = Board(mock_pieces, "B")
    assert board.has_piece("0") is True
    assert board.has_piece("4") is False

def test_get_row_number():
    board = Board([], "W")
    # posição 0 está na row 0, posição 8 na row 2 (cada row tem 4 colunas escuras)
    assert board.get_row_number(0) == 0
    assert board.get_row_number(8) == 2

def test_get_col_number():
    board = Board([], "W")
    # Testando col_number (varia conforme paridade da row)
    assert board.get_col_number(0) in range(0,8)

from unittest.mock import Mock

def test_get_row():
    # Criando mocks para as peças
    mock_pieces = [Mock(spec=Piece) for _ in range(4)]
    mock_pieces[0].get_position.return_value = "0"
    mock_pieces[1].get_position.return_value = "1"
    mock_pieces[2].get_position.return_value = "4" 
    mock_pieces[3].get_position.return_value = "5"  

    board = Board(mock_pieces, "B")

    row0 = board.get_row(0) 
    assert len(row0) == 2



def test_get_pieces_by_coords(mock_pieces):
    board = Board(mock_pieces, "W")
    # Ex: posição 0BN -> row=0, col depende da função
    res = board.get_pieces_by_coords((0,0))
    assert len(res) == 1
