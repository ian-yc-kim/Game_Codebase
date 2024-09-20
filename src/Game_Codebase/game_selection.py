import tkinter as tk
import subprocess


def launch_snake_game():
    subprocess.Popen(['python', 'src/Game_Codebase/main.py'])


def create_game_selection_ui():
    root = tk.Tk()
    root.title('Game Selection')
    root.geometry('300x150')

    play_snake_button = tk.Button(root, text='Play Snake Game', command=launch_snake_game)
    play_snake_button.pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    create_game_selection_ui()
