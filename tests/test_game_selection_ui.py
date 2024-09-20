import pytest
import tkinter as tk
from Game_Codebase.game_selection_ui import create_game_selection_ui

def test_game_selection_ui(mocker):
    mock_tk = mocker.patch('tkinter.Tk', autospec=True)
    mocker.patch('tkinter.Button', autospec=True)

    create_game_selection_ui()

    mock_tk.assert_called_once()
    tk.Button.assert_called_once_with(mock_tk.return_value, text='Play Snake Game', command=mocker.ANY)
    mock_tk.return_value.mainloop.assert_called_once()
