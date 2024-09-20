import tkinter as tk
from Game_Codebase.main import gameLoop


def launch_snake_game():
    gameLoop()


def create_game_selection_ui():
    root = tk.Tk()
    root.title('Game Selection')

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    play_snake_button = tk.Button(frame, text='Play Snake Game', command=launch_snake_game)
    play_snake_button.pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    create_game_selection_ui()
