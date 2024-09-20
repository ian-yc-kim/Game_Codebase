import pytest
import pygame
from Game_Codebase.main import display_score

@pytest.fixture(autouse=True)
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_display_score(mocker):
    mock_font = mocker.Mock()
    mock_surface = mocker.Mock(spec=pygame.Surface)
    mock_font.render.return_value = mock_surface
    mocker.patch('Game_Codebase.main.score_font', mock_font)

    mock_display = mocker.Mock(spec=pygame.Surface)
    mocker.patch('Game_Codebase.main.display', mock_display)

    from Game_Codebase.main import display_score
    display_score(10)

    mock_font.render.assert_called_once_with('Your Score: 10', True, (0, 0, 0))
    mock_display.blit.assert_called_once_with(mock_surface, [10, 10])


def test_score_increase(mocker):
    mocker.patch('pygame.init')
    mock_surface = mocker.Mock()
    mocker.patch('pygame.display.set_mode', return_value=mock_surface)
    mocker.patch('pygame.time.Clock')
    mocker.patch('pygame.display.update')
    mocker.patch('pygame.event.get', return_value=[])
    mocker.patch('pygame.draw.rect')
    mocker.patch('Game_Codebase.main.our_snake')
    mocker.patch('Game_Codebase.main.display_score')
    mocker.patch('Game_Codebase.main.quit')  # Mock the quit function

    from Game_Codebase.main import gameLoop

    mocker.patch('random.randrange', side_effect=[400, 300, 400, 300])
    mocker.patch('pygame.time.get_ticks', side_effect=[0, 100, 200, 300])

    mock_quit_event = mocker.Mock()
    mock_quit_event.type = pygame.QUIT
    mocker.patch('pygame.event.get', return_value=[mock_quit_event])

    gameLoop()

    # Add assertions here to check if the score increased
    # For example: assert Game_Codebase.main.get_score() > 0
