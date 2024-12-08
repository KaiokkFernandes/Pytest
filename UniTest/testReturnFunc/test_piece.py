import pytest
from unittest.mock import Mock

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../python-checkers')))

from piece import Piece


@pytest.fixture
def mock_board():
    # Cria um mock para o tabuleiro, configurando alguns comportamentos padrão
    board = Mock()
    board.get_col_number.side_effect = lambda pos: int(str(pos)[1])  # Retorna o número da coluna a partir da posição
    board.get_row_number.side_effect = lambda pos: int(str(pos)[0])  # Retorna o número da linha a partir da posição
    board.get_color_up.return_value = "W"  # Assume que a cor "W" está para cima no tabuleiro
    board.has_piece.return_value = False  # Nenhuma peça no tabuleiro por padrão
    board.get_pieces_by_coords.side_effect = lambda *coords: [None] * len(coords)  # Nenhuma peça nas coordenadas fornecidas
    return board


def test_get_position():
    # Testa o método get_position da peça, que deve retornar a posição da peça
    piece = Piece("20WN")  # Cria uma peça na posição 20
    assert piece.get_position() == "20"  # Verifica se a posição é 20


def test_get_color():
    # Testa o método get_color da peça, que deve retornar a cor da peça
    piece = Piece("20WN")  # Cria uma peça da cor "W" (branca)
    assert piece.get_color() == "W"  # Verifica se a cor da peça é "W"


def test_is_king():
    # Testa o método is_king da peça, verificando se ela é uma peça "rei"
    piece = Piece("20WN")  # Cria uma peça normal
    assert not piece.is_king()  # Verifica se a peça não é um rei
    piece.set_is_king(True)  # Define a peça como sendo um rei
    assert piece.is_king()  # Verifica se a peça agora é um rei


def test_set_position():
    # Testa o método set_position da peça, que deve definir a posição da peça
    piece = Piece("20WN")  # Cria uma peça na posição 20
    piece.set_position(30)  # Define a nova posição como 30
    assert piece.get_position() == "30"  # Verifica se a posição foi atualizada corretamente para 30


def test_get_adjacent_squares(mock_board):
    # Testa o método get_adjacent_squares da peça, que deve retornar as casas adjacentes
    mock_board.get_col_number.side_effect = lambda pos: pos % 10  # Simula o cálculo da coluna
    mock_board.get_row_number.side_effect = lambda pos: pos // 10  # Simula o cálculo da linha
    piece = Piece("20WN")  # Cria uma peça na posição 20
    adjacent_squares = piece.get_adjacent_squares(mock_board)  # Obtém as casas adjacentes à peça
    assert len(adjacent_squares) == 2  # Verifica se o número de casas adjacentes é 2 (ajuste conforme esperado)


def test_get_moves_empty_board(mock_board):
    # Testa o método get_moves da peça quando o tabuleiro está vazio
    mock_board.get_pieces_by_coords.side_effect = lambda *coords: [None] * len(coords)  # Simula tabuleiro vazio
    mock_board.get_col_number.side_effect = lambda pos: pos % 10  # Simula o cálculo da coluna
    mock_board.get_row_number.side_effect = lambda pos: pos // 10  # Simula o cálculo da linha
    piece = Piece("20WN")  # Cria uma peça na posição 20
    moves = piece.get_moves(mock_board)  # Obtém os movimentos da peça no tabuleiro vazio
    assert len(moves) == 2  # Verifica se existem 2 movimentos possíveis (ajuste conforme esperado)


def test_get_moves_with_eating(mock_board):
    # Testa o método get_moves da peça com captura de outra peça
    piece = Piece("20WN")  # Cria uma peça na posição 20
    mock_board.get_pieces_by_coords.side_effect = lambda *coords: [
        Mock(get_color=lambda: "B", get_position=lambda: "31"),  # Simula uma peça adversária na posição 31
        None,  # Simula uma posição vazia
    ]
    mock_board.has_piece.side_effect = lambda pos: pos != 42  # Simula que a posição 42 está livre
    mock_board.get_col_number.side_effect = lambda pos: pos % 10  # Simula o cálculo da coluna
    mock_board.get_row_number.side_effect = lambda pos: pos // 10  # Simula o cálculo da linha

    moves = piece.get_moves(mock_board)  # Obtém os movimentos da peça com base nas peças no tabuleiro
    assert len(moves) == 1  # Verifica se a peça pode capturar uma peça adversária (ajuste conforme a lógica real)
