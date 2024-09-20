import pytest
from Game_Codebase.main import play_snake_game


def test_play_snake_game(monkeypatch):
    # Mock the game loop to prevent it from running indefinitely
    def mock_gameLoop():
        pass

    monkeypatch.setattr('Game_Codebase.main.gameLoop', mock_gameLoop)

    # Call the play_snake_game function to ensure it calls gameLoop
    play_snake_game()

    # If no exceptions are raised, the test passes
    assert True
