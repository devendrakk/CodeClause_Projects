import random
import tkinter as tk
from tkinter import messagebox

# Function to start the game
def start_game():
    global number_to_guess, attempts, max_attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 3
    guess_entry.config(state=tk.NORMAL)
    guess_button.config(state=tk.NORMAL)
    feedback_label.config(text="Guess the number between 1 and 100", fg="blue")
    attempts_label.config(text=f"Remaining attempts: {max_attempts}")
    guess_entry.delete(0, tk.END)

# Function to check the user's guess
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        remaining_attempts = max_attempts - attempts

        if guess < number_to_guess:
            feedback_label.config(text="Too low! Try again.", fg="red")
        elif guess > number_to_guess:
            feedback_label.config(text="Too high! Try again.", fg="red")
        else:
            feedback_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.", fg="green")
            guess_entry.config(state=tk.DISABLED)
            guess_button.config(state=tk.DISABLED)
            messagebox.showinfo("Congratulations", f"You guessed the number in {attempts} attempts!")
            return

        if attempts < max_attempts:
            attempts_label.config(text=f"Remaining attempts: {remaining_attempts}")
        else:
            feedback_label.config(text=f"Game over! The correct number was {number_to_guess}.", fg="red")
            guess_entry.config(state=tk.DISABLED)
            guess_button.config(state=tk.DISABLED)
            messagebox.showinfo("Game Over", f"You've used all your attempts. The correct number was {number_to_guess}.")

    except ValueError:
        feedback_label.config(text="Invalid input! Please enter a valid integer.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="lightblue")

# Create and place widgets
title_label = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 18, "bold"), bg="lightblue")
title_label.pack(pady=10)

feedback_label = tk.Label(root, text="Guess the number between 1 and 100", font=("Helvetica", 12), bg="lightblue")
feedback_label.pack(pady=10)

attempts_label = tk.Label(root, text="Remaining attempts: 3", font=("Helvetica", 12), bg="lightblue")
attempts_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Helvetica", 14), width=5)
guess_entry.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", font=("Helvetica", 14), command=check_guess)
guess_button.pack(pady=10)

restart_button = tk.Button(root, text="Restart Game", font=("Helvetica", 14), command=start_game)
restart_button.pack(pady=10)

# Start the game for the first time
start_game()

# Run the main event loop
root.mainloop()
