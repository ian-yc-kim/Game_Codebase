import pygame
import pytest
from Game_Codebase.main import display_score


def test_display_score(mocker):
    mock_font = mocker.Mock()
    mock_surface = mocker.Mock(spec=pygame.Surface)
    mock_font.render.return_value = mock_surface
    mocker.patch('Game_Codebase.main.score_font', mock_font)

    mock_display = mocker.Mock(spec=pygame.Surface)

    display_score(mock_display, 10)

    mock_font.render.assert_called_once_with('Your Score: 10', True, (0, 0, 0))
    mock_display.blit.assert_called_once_with(mock_surface, [10, 10])
