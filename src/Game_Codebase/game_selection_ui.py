import tkinter as tk
from tkinter import messagebox
import subprocess

__all__ = ['create_game_selection_ui']


def create_main_window():
    """
    Creates the main window for the game selection UI.

    Returns:
        root (tk.Tk): The main Tkinter window object.
        frame (tk.Frame): The frame within the main window.
    """
    root = tk.Tk()
    root.title('Game Selection')
    root.geometry('300x200')
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    return root, frame


def add_play_snake_button(frame):
    """
    Adds a button to the frame to play the Snake game.

    Args:
        frame (tk.Frame): The frame to which the button will be added.
    """
    play_button = tk.Button(frame, text='Play Snake Game', command=launch_snake_game)
    play_button.pack(pady=20)


def launch_snake_game():
    """
    Launches the Snake game by running the main.py script.
    Displays an error message if the game fails to launch.
    """
    try:
        subprocess.Popen(['python', 'main.py'])
    except Exception as e:
        messagebox.showerror('Error', f'Failed to launch the snake game: {e}')


def create_game_selection_ui():
    """
    Creates and runs the game selection UI.
    """
    root, frame = create_main_window()
    add_play_snake_button(frame)
    root.mainloop()


if __name__ == '__main__':
    create_game_selection_ui()
