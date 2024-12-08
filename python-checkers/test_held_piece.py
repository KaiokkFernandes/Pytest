import pytest
from held_piece import HeldPiece
import pygame

def test_check_collision():
    surface = pygame.Surface((50,50))
    hp = HeldPiece(surface, (0,0))
    # Rects possíveis
    rect_list = [pygame.Rect(0,0,50,50), pygame.Rect(60,60,50,50)]
    # Mouse é mockado pelo get_pos do pygame
    hp.draw_rect.x = 10
    hp.draw_rect.y = 10
    collided = hp.check_collision(rect_list)
    assert collided == rect_list[0]
