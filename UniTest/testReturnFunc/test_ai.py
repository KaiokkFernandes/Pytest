import pytest
from unittest.mock import Mock
from ai import AI
from board import Board
from piece import Piece

@pytest.fixture
def mock_board_winner_none():
    # Mock de board sem vencedor e com peças equilibradas
    board = Mock(spec=Board)
    board.get_winner.return_value = None
    board.get_pieces.return_value = [Mock(spec=Piece) for _ in range(4)]
    board.get_color_up.return_value = 'W'
    return board

@pytest.fixture
def mock_board_with_winner():
    # Mock de board com um vencedor
    board = Mock(spec=Board)
    board.get_winner.return_value = 'W'
    # Simulando que a primeira peça é branca
    p = Mock(spec=Piece)
    p.get_color.return_value = 'W'
    board.get_pieces.return_value = [p]
    return board

def test_minimax_returns_value(mock_board_winner_none):
    ai = AI('W')
    # Simulando que get_value será chamado logo, pois depth=0
    mock_board_winner_none.get_winner.return_value = None
    # get_value será chamado, então vamos testar o retorno
    ai.get_value = Mock(return_value=1)
    result = ai.minimax(mock_board_winner_none, True, 0, 'W')
    assert isinstance(result, int)

def test_get_move_returns_dict(mock_board_winner_none):
    ai = AI('W')
    # Mockando movimentos possíveis
    piece = Mock(spec=Piece)
    piece.get_color.return_value = 'W'
    piece.get_position.return_value = '20'
    piece.get_moves.return_value = [{"position": "21", "eats_piece": False}]
    mock_board_winner_none.get_pieces.return_value = [piece]
    ai.minimax = Mock(return_value=1)  # Minimizar complexidade
    
    move = ai.get_move(mock_board_winner_none)
    assert isinstance(move, dict)
    assert "position_to" in move
    assert "position_from" in move

def test_get_value_returns_int(mock_board_with_winner):
    ai = AI('W')
    val = ai.get_value(mock_board_with_winner)
    assert isinstance(val, int)
    # Como o vencedor é W e o AI é W, valor deve ser 2
    assert val == 2
