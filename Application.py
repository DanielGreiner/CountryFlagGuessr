import json
import os
import sys
import tkinter as tk
from tkinter import messagebox

#from PIL import Image, ImageTk

regions = ['Africa', 'Asia', 'Caribbean', 'Europe', 'North America', 'Oceania', 'South America'] #, 'World']
flag_dir = 'country_flags'


class GuessrApp:
    def __init__(self, root, data=None):
        self.root = root
        self.root.title('Flag to country. A guessr game')
        self.root.geometry('800x700')
        self.root.configure(bg='LightBlue')
        self.root.resizable(False, False)

        self.data = data
        self.score = 0
        self.total_questions = 0
        self.current_questions = 0
        self.num_answers = 4
        self.countries_dict = {}
        self.correct_answer = None

        self.button1 = tk.Button(self.root, text='Button 1', width=40, command=lambda: self.check_answer(0))
        self.button1 = tk.Button(self.root, text='Button 2', width=40, command=lambda: self.check_answer(1))
        self.button1 = tk.Button(self.root, text='Button 3', width=40, command=lambda: self.check_answer(2))
        self.button1 = tk.Button(self.root, text='Button 4', width=40, command=lambda: self.check_answer(3))
        self.flag_label = tk.Label(self.root)

        # Initialize score label outside of challenge start to avoid overwriting
        self.score_label = tk.Label(self.root, text="Questions: 0 | Correct: 0 | Percentage: 0%")
        self.score_label.grid(row=5, column=0, columnspan=5, pady=10)

        # Hide all buttons initially
        self.hide_buttons()

        # Load country data
        self.file_path = 'AllCountries.json'
        if os.path.exists(self.file_path):
            self.read_json_file(self.file_path)
        else:
            messagebox.showerror("Error", f"File not found: {self.file_path}")
            sys.exit()  # Exit the program if the file doesn't exist

    def read_json_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
        except json.JSONDecodeError:
            print("Error: The file could not be decoded. Check if it's a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def hide_buttons(self):
        self.button1.grid_forget()
        self.button2.grid_forget()
        self.button3.grid_forget()
        self.button4.grid_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessrApp(root)
    root.mainloop()
