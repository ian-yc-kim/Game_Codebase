import pytest
from unittest.mock import patch, MagicMock
from Game_Codebase.game_selection_ui import create_game_selection_ui


def test_create_game_selection_ui(mocker):
    # Mock Tk and its methods
    mock_tk = mocker.patch('Game_Codebase.game_selection_ui.tk')
    mock_root = MagicMock()
    mock_tk.Tk.return_value = mock_root

    # Mock Frame and Button
    mock_frame = MagicMock()
    mock_button = MagicMock()
    mock_tk.Frame.return_value = mock_frame
    mock_tk.Button.return_value = mock_button

    # Call the function
    create_game_selection_ui()

    # Assert that Tk was initialized
    mock_tk.Tk.assert_called_once()

    # Assert that the window title was set
    mock_root.title.assert_called_once_with('Game Selection')

    # Assert that Frame was created and packed
    mock_tk.Frame.assert_called_once_with(mock_root)
    mock_frame.pack.assert_called_once_with(fill=mock_tk.BOTH, expand=True, padx=10, pady=10)

    # Assert that Button was created with correct text and command
    mock_tk.Button.assert_called_once_with(mock_frame, text='Play Snake Game', command=mocker.ANY)
    mock_button.pack.assert_called_once_with(pady=20)

    # Assert that mainloop was called
    mock_root.mainloop.assert_called_once()
