import tkinter as tk
import random

class StylishGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#2b2d42")  # Dark background

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(
            root, text="Guess the Number!", font=("Helvetica", 20, "bold"),
            fg="#edf2f4", bg="#2b2d42"
        )
        self.title_label.pack(pady=15)

        self.instruction = tk.Label(
            root, text="Enter a number between 1 and 100:", font=("Helvetica", 12),
            fg="#8d99ae", bg="#2b2d42"
        )
        self.instruction.pack(pady=5)

        self.entry = tk.Entry(root, font=("Helvetica", 14), width=10, justify="center")
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(
            root, text="Submit Guess", font=("Helvetica", 12, "bold"),
            bg="#ef233c", fg="white", activebackground="#d90429", relief="flat",
            command=self.check_guess
        )
        self.submit_button.pack(pady=10)

        self.result = tk.Label(
            root, text="", font=("Helvetica", 12),
            fg="white", bg="#2b2d42"
        )
        self.result.pack(pady=10)

        self.restart_button = tk.Button(
            root, text="Restart", font=("Helvetica", 10),
            command=self.restart_game, bg="#8d99ae", fg="black", relief="flat"
        )
        self.restart_button.pack(pady=5)
        self.restart_button.config(state=tk.DISABLED)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.number_to_guess:
                self.result.config(text="📉 Too low!")
            elif guess > self.number_to_guess:
                self.result.config(text="📈 Too high!")
            else:
                self.result.config(text=f"🎉 Correct in {self.attempts} attempts!")
                self.submit_button.config(state=tk.DISABLED)
                self.restart_button.config(state=tk.NORMAL)
        except ValueError:
            self.result.config(text="⚠️ Enter a valid number.")

    def restart_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.result.config(text="")
        self.entry.delete(0, tk.END)
        self.submit_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = StylishGuessingGame(root)
    root.mainloop()
