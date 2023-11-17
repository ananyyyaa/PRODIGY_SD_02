import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("NUMBER GUESSING GAME")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="GUESS A NUMBER BETWEEN 1 TO 100")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="ENTER", command=self.check_guess)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = int(self.entry.get())

        if guess == self.secret_number:
            self.attempts += 1
            self.result_label.config(text=f"CONGRATULATIONS! You guessed the number in {self.attempts} attempts.")
            self.submit_button.config(state=tk.DISABLED)  
        elif guess < self.secret_number:
            self.attempts += 1
            self.result_label.config(text="Too low! Try again.")
        else:
            self.attempts += 1
            self.result_label.config(text="Too high! Try again.")



if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
