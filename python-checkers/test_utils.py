import pytest
from utils import get_position_with_row_col, get_piece_position, get_piece_gui_coords, get_surface_mouse_offset

def test_get_position_with_row_col():
    pos = get_position_with_row_col(0,0)
    assert pos == 0
    pos2 = get_position_with_row_col(2,2)
    assert isinstance(pos2, int)

def test_get_piece_position():
    pos = get_piece_position((100,100), 56, (34,34))
    assert isinstance(pos, int)

def test_get_piece_gui_coords():
    coords = get_piece_gui_coords((0,0), 56, (34,34))
    assert isinstance(coords, tuple)
    assert len(coords) == 2

def test_get_surface_mouse_offset():
    offset = get_surface_mouse_offset((50,50),(45,45))
    assert offset == (5,5)
