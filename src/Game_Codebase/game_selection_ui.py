import tkinter as tk
from tkinter import messagebox
import subprocess

__all__ = ['create_game_selection_ui']


def create_main_window():
    root = tk.Tk()
    root.title('Game Selection')
    root.geometry('300x200')
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    return root, frame


def add_play_snake_button(frame):
    play_button = tk.Button(frame, text='Play Snake Game', command=launch_snake_game)
    play_button.pack(pady=20)


def launch_snake_game():
    try:
        subprocess.Popen(['python', 'main.py'])
    except Exception as e:
        messagebox.showerror('Error', f'Failed to launch the snake game: {e}')


def create_game_selection_ui():
    root, frame = create_main_window()
    add_play_snake_button(frame)
    root.mainloop()


if __name__ == '__main__':
    create_game_selection_ui()
