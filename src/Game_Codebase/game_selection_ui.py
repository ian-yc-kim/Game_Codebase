import tkinter as tk
from Game_Codebase.main import gameLoop


def launch_snake_game():
    gameLoop()


def create_game_selection_ui():
    root = tk.Tk()
    root.title('Game Selection')

    play_snake_button = tk.Button(root, text='Play Snake Game', command=launch_snake_game)
    play_snake_button.pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    create_game_selection_ui()
