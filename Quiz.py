import tkinter as tk
from tkinter import messagebox

# Sample questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Program Unit", "Central Processing Unit", "Control Panel Unit", "Compute Processing Unit"],
        "answer": "Central Processing Unit"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Fun Quiz App")
        self.root.geometry("600x450")
        self.root.config(bg="#f0f8ff")

        self.current_q = 0
        self.score = 0
        self.user_answer = tk.StringVar()

        self.welcome_screen()

    def welcome_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the Quiz!", font=("Comic Sans MS", 20, "bold"), bg="#f0f8ff", fg="#333").pack(pady=30)
        tk.Button(self.root, text="Start Quiz 🚀", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10, command=self.start_quiz).pack()

    def start_quiz(self):
        self.clear_screen()
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 16, "bold"), bg="#f0f8ff", wraplength=500, justify="left", fg="#333")
        self.question_label.pack(pady=30)

        self.radio_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.user_answer,
                                 font=("Arial", 13), value="", anchor="w",
                                 bg="#f0f8ff", activebackground="#e0ffff", highlightthickness=0)
            btn.pack(fill="x", padx=60, pady=5)
            self.radio_buttons.append(btn)

        self.progress_label = tk.Label(self.root, text="", font=("Arial", 11, "italic"), bg="#f0f8ff", fg="#666")
        self.progress_label.pack(pady=10)

        self.nav_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.nav_frame.pack(pady=10)

        self.next_btn = tk.Button(self.nav_frame, text="Next ➡️", font=("Arial", 12, "bold"),
                                  bg="#007BFF", fg="white", padx=15, pady=5,
                                  command=self.next_question)
        self.next_btn.grid(row=0, column=0, padx=10)

    def display_question(self):
        q = questions[self.current_q]
        self.question_label.config(text=f"Q{self.current_q + 1}: {q['question']}")
        self.progress_label.config(text=f"Question {self.current_q + 1} of {len(questions)}")
        self.user_answer.set(None)
        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option, value=option)

    def next_question(self):
        selected = self.user_answer.get()
        if not selected:
            messagebox.showwarning("⚠️ Warning", "Please select an answer!")
            return

        correct = questions[self.current_q]["answer"]
        if selected == correct:
            self.score += 1

        self.current_q += 1
        if self.current_q < len(questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_screen()
        result_text = f"🎉 You scored {self.score} out of {len(questions)}"
        tk.Label(self.root, text="Quiz Completed!", font=("Comic Sans MS", 20, "bold"), fg="#333", bg="#f0f8ff").pack(pady=30)
        tk.Label(self.root, text=result_text, font=("Arial", 16), bg="#f0f8ff", fg="#2E8B57").pack(pady=10)
        tk.Button(self.root, text="Exit ❌", command=self.root.destroy,
                  font=("Arial", 12), bg="#DC3545", fg="white", padx=20, pady=8).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()