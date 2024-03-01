from tkinter import *
import random
import pygame

from tkinter import messagebox

import pygame.mixer

from PIL import Image, ImageTk

pygame.mixer.init()
easy = False
medium = False
hard = False
attempts = None
pygame.mixer.music.load('images/music/sitcom.mp3')
from tkinter import messagebox

while True:
    pygame.mixer.music.play(-1)

    def check_answer(entry_window, btn_check, text, easy, medium, hard, answer):
        global attempts

        if easy:
            max_value = 10
        elif medium:
            max_value = 30
        elif hard:
            max_value = 60

        attempts.set(attempts.get() - 1)

        try:
            guess = int(entry_window.get())
            if guess < 1 or guess > max_value:
                raise ValueError(f"Invalid value. Please enter a number between 1 and {max_value}")
            elif guess == answer:
                text.set("You win! Congrats!!")
                btn_check.pack_forget()
            elif attempts.get() == 0:
                text.set("You are out of attempts!")
                btn_check.pack_forget()
            elif guess < answer:
                text.set(f"Incorrect! You have {attempts.get()} attempts remaining - Go Higher!!")
            elif guess > answer:
                text.set(f"Incorrect! You have {attempts.get()} attempts remaining - Go Lower!!")
        except ValueError as e:
            messagebox.showinfo("Invalid Value", f"Invalid value. Please enter a number between 1 and {max_value}")


    def start_game_easy(diff_screen, easy):
        global attempts
        easy = True
        attempts = IntVar()
        attempts.set(3)
        answer = int(random.randint(1, 10))
        diff_screen.destroy()
        game_screen = Tk()
        game_screen.title("Guess the Number")
        game_screen.geometry("960x540")
        game_screen.resizable(False, False)

        image_easy = Image.open("images/bg.png")
        photo = ImageTk.PhotoImage(image_easy)

        background_label = Label(game_screen, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = Label(game_screen, text="Guess the number between 1 and 10", font=("Papyrus", 25), background=("#fafad2"),
                      fg="#663300")
        label.pack(pady=20)

        entry_window = Entry(game_screen, width=40, borderwidth=4, font=("Papyrus", 14), background=("#f9f9e6"))
        entry_window.pack(pady=5)

        text = StringVar()
        text.set("You have 3 attempts remaining! Good luck!")
        guess_attempts = Label(game_screen, textvariable=text, font=("Papyrus", 14), background=("#c5ddd1"))
        guess_attempts.pack(pady=10)

        btn_check = Button(game_screen, text="Check",
                           command=lambda: check_answer(entry_window, btn_check, text, easy, medium, hard, answer),
                           font=("Papyrus", 14), background=("#c5ddd1"))
        btn_check.pack(pady=6)

        btn_quit = Button(game_screen, text="Quit", command=game_screen.destroy, font=("Papyrus", 14),
                          background=("#fadf9b"))
        btn_quit.pack()

        game_screen.mainloop()


    def start_game_medium(diff_screen, medium):
        global attempts  # Объявляем переменную attempts как глобальную
        medium = True
        attempts = IntVar()
        attempts.set(8)
        answer = int(random.randint(1, 30))
        diff_screen.destroy()  # Close the menu screen
        game_screen = Tk()
        game_screen.title("Guess the Number")
        game_screen.geometry("960x540")
        game_screen.resizable(False, False)

        image_medium = Image.open("images/bg.png")
        photo = ImageTk.PhotoImage(image_medium)

        background_label = Label(game_screen, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = Label(game_screen, text="Guess the number between 1 and 30", font=("Papyrus", 25), background=("#fafad2"),
                      fg="#663300")
        label.pack(pady=20)

        entry_window = Entry(game_screen, width=40, borderwidth=4, font=("Papyrus", 14), background=("#f9f9e6"))
        entry_window.pack(pady=5)

        text = StringVar()
        text.set("You have 8 attempts remaining! Good luck!")
        guess_attempts = Label(game_screen, textvariable=text, font=("Papyrus", 14), background=("#c5ddd1"))
        guess_attempts.pack(pady=10)

        btn_check = Button(game_screen, text="Check",
                           command=lambda: check_answer(entry_window, btn_check, text, easy, medium, hard, answer),
                           font=("Papyrus", 14), background=("#c5ddd1"))
        btn_check.pack(pady=6)

        btn_quit = Button(game_screen, text="Quit", command=game_screen.destroy, font=("Papyrus", 14),
                          background=("#fadf9b"))
        btn_quit.pack()

        game_screen.mainloop()


    def start_game_hard(diff_screen, hard):
        global attempts
        hard = True
        attempts = IntVar()
        attempts.set(12)
        answer = int(random.randint(1, 60))
        diff_screen.destroy()  # Close the menu screen
        game_screen = Tk()
        game_screen.title("Guess the Number")
        game_screen.geometry("960x540")
        game_screen.resizable(False, False)

        image_hard = Image.open("images/bg.png")
        photo = ImageTk.PhotoImage(image_hard)

        background_label = Label(game_screen, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = Label(game_screen, text="Guess the number between 1 and 60", font=("Papyrus", 25), background=("#fafad2"),
                      fg="#663300")
        label.pack(pady=20)

        entry_window = Entry(game_screen, width=40, borderwidth=4, font=("Papyrus", 14), background=("#f9f9e6"))
        entry_window.pack(pady=5)

        text = StringVar()
        text.set("You have 12 attempts remaining! Good luck!")
        guess_attempts = Label(game_screen, textvariable=text, font=("Papyrus", 14), background=("#c5ddd1"))
        guess_attempts.pack(pady=10)

        btn_check = Button(game_screen, text="Check",
                           command=lambda: check_answer(entry_window, btn_check, text, easy, medium, hard, answer),
                           font=("Papyrus", 14), background=("#c5ddd1"))
        btn_check.pack(pady=6)

        btn_quit = Button(game_screen, text="Quit", command=game_screen.destroy, font=("Papyrus", 14),
                          background=("#fadf9b"))
        btn_quit.pack(pady=10)

        game_screen.mainloop()


    def diff_game(menu_screen):
        menu_screen.destroy()  # Close the menu screen
        diff_screen = Tk()
        diff_screen.title("Difficulty")
        diff_screen.geometry("960x540")
        diff_screen.resizable(False, False)
        image_diff = Image.open("images/bg.png")
        photo = ImageTk.PhotoImage(image_main)

        background_label = Label(diff_screen, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = Label(diff_screen, text="Choose the difficulty for game", font=("Papyrus", 30),
                      background=("#fafad2"), fg="#663300")
        label.pack(pady=25)

        btn_check1 = Button(diff_screen, text="Easy peasy", command=lambda: start_game_easy(diff_screen, easy),
                            font=("Papyrus", 14), background=("#c5ddd1"))
        btn_check1.pack(pady=6)
        btn_check2 = Button(diff_screen, text="Medium", command=lambda: start_game_medium(diff_screen, medium),
                            font=("Papyrus", 14), background=("#c5ddd1"))
        btn_check2.pack(pady=6)
        btn_check3 = Button(diff_screen, text="Hard", command=lambda: start_game_hard(diff_screen, hard),
                            font=("Papyrus", 14), background=("#c5ddd1"))
        btn_check3.pack(pady=6)

        btn_quit = Button(diff_screen, text="Quit", command=diff_screen.destroy, font=("Papyrus", 14),
                          background=("#fadf9b"))
        btn_quit.pack(pady=10)

        diff_screen.mainloop()


    menu_screen = Tk()
    menu_screen.title("Guess the Number Menu")
    menu_screen.geometry("960x540")
    menu_screen.resizable(False, False)

    image_main = Image.open("images/bg.png")
    photo = ImageTk.PhotoImage(image_main)

    background_label = Label(menu_screen, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry_label = Label(menu_screen, text="Welcome to Guess the Number Game!", font=("Papyrus", 30),
                        background=("#fafad2"), fg="#663300")
    entry_label.pack(pady=20)

    btn_start = Button(menu_screen, text="Start Game", command=lambda: diff_game(menu_screen), font=("Papyrus", 14),
                       background=("#c5ddd1"))
    btn_start.pack(pady=10)

    btn_quit = Button(menu_screen, text="Quit", command=menu_screen.destroy, font=("Papyrus", 14),
                      background=("#fadf9b"))
    btn_quit.pack()

    menu_screen.mainloop()