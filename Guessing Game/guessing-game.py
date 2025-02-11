import random
import tkinter as tk
from tkinter import messagebox

# Generate a random number between 1 and 100
jackpot = random.randint(1, 100)
attempts = 0  # Track number of attempts


# Function to handle guess logic
def logic_guess():
    global attempts
    try:
        guess = int(guess_input.get())
        attempts += 1

        if guess == jackpot:
            messagebox.showinfo('Congratulations!', f'You guessed the correct number in {attempts} attempts!')
            reset_game()
        elif guess < jackpot:
            messagebox.showwarning('Try Again', 'Guess Higher!')
        else:
            messagebox.showwarning('Try Again', 'Guess Lower!')
    except ValueError:
        messagebox.showerror('Invalid Input', 'Please enter a valid number.')


# Function to reset the game
def reset_game():
    global jackpot, attempts
    jackpot = random.randint(1, 100)
    attempts = 0
    guess_input.delete(0, tk.END)


# Setting up the GUI
root = tk.Tk()
root.title('Guessing Game')
root.geometry('400x400')
root.config(bg='#1e1e2e')
root.iconbitmap('game favicon.ico')

# Styling
frame = tk.Frame(root, bg='#282a36', padx=20, pady=20)
frame.pack(expand=True)

heading = tk.Label(frame, text='Guess the Number', fg='#50fa7b', bg='#282a36', font=('Arial', 18, 'bold'))
heading.pack(pady=10)

guess_label = tk.Label(frame, text='Enter a number (1-100):', fg='white', bg='#282a36', font=('Arial', 12))
guess_label.pack()

guess_input = tk.Entry(frame, width=10, font=('Arial', 14), justify='center')
guess_input.pack(pady=5)

guess_button = tk.Button(frame, text='Guess', command=logic_guess, font=('Arial', 12, 'bold'), bg='#ff5555', fg='white',
                         width=10)
guess_button.pack(pady=10)

reset_button = tk.Button(frame, text='Reset', command=reset_game, font=('Arial', 12, 'bold'), bg='#6272a4', fg='white',
                         width=10)
reset_button.pack(pady=5)

root.mainloop()