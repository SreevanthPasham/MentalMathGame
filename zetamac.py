import tkinter as tk
import random

class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Speed Challenge")
        self.root.geometry("550x500")
        self.root.resizable(False, False)

        self.problems_list = []

        self.current_problem = None
        self.current_problem_index = 0
        self.score = 0
        self.time_left = 30
        self.timer_running = False
        
        self.setup_ui()

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.start_frame = tk.Frame(self.main_frame)
        self.start_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(self.start_frame, text="Math Speed Challenge", font=("Arial", 18, "bold")).pack(pady=10)
    
        instructions = tk.Label(self.start_frame, text="Test your math skills with these arithmetic problems:\n\n"
"• Addition and subtraction with numbers 2-100\n"
"• Multiplication with numbers 2-12 × 2-100\n"
"• Division with numbers 2-100 ÷ 2-12\n\n"
"You'll have 30 seconds to solve as many problems as you can!\n"
"The game will automatically submit when you enter the correct answer.",
        justify=tk.LEFT, wraplength=500)
        instructions.pack(pady=10)
    
        self.start_button = tk.Button(self.start_frame, text="Start Game", font=("Arial", 12, "bold"), bg="#48bb78", fg="black", padx=20, pady=10, command=self.start_game)
        self.start_button.pack(pady=20)
    
        self.game_frame = tk.Frame(self.main_frame)
        self.info_frame = tk.Frame(self.game_frame)
        self.info_frame.pack(fill=tk.X, pady=10)
        self.problem_counter = tk.Label(self.info_frame, text="Problem: 1", font=("Arial", 10, "bold"),
bg="#d1d5db", fg="black", padx=10,
pady=5)
        self.problem_counter.pack(side=tk.LEFT)
        self.timer_display = tk.Label(self.info_frame, text="Time: 30s",
font=("Arial", 10, "bold"),
bg="#d1d5db", fg="black", padx=10,
pady=5)
        self.timer_display.pack(side=tk.LEFT, padx=20)
        self.score_display = tk.Label(self.info_frame, text="Score: 0",
font=("Arial", 10, "bold"),
bg="#d1d5db", fg="black", padx=10,
pady=5)
        self.score_display.pack(side=tk.LEFT)
        self.progress_frame = tk.Frame(self.game_frame, height=10,
bg="#9ca3af")
        self.progress_frame.pack(fill=tk.X, pady=10)
        self.progress_bar = tk.Frame(self.progress_frame, height=10,
bg="#48bb78")
        self.progress_bar.place(relwidth=1, relheight=1)
        self.problem_display = tk.Label(self.game_frame, text="", font=
("Arial", 24, "bold"))
        self.problem_display.pack(pady=20)
        self.input_frame = tk.Frame(self.game_frame)
        self.input_frame.pack(pady=10)
        self.answer_var = tk.StringVar()
        self.answer_var.trace("w", self.check_answer_on_change)
        self.answer_entry = tk.Entry(self.input_frame,
textvariable=self.answer_var,
font=("Arial", 14), width=15,
justify=tk.CENTER)
        self.answer_entry.pack(side=tk.LEFT, padx=5)
        self.submit_button = tk.Button(self.input_frame, text="Submit",
font=("Arial", 12),
bg="#4299e1", fg="white", padx=10,
pady=5,
command=lambda:
self.validate_and_process_answer(self.answer_var.get()))
        self.submit_button.pack(side=tk.LEFT)
        self.feedback_message = tk.Label(self.game_frame, text="", font=
("Arial", 12, "bold"), fg="#38a169")
        self.feedback_message.pack(pady=10)
        self.end_frame = tk.Frame(self.main_frame)
        tk.Label(self.end_frame, text="Game Over!", font=("Arial", 18,
"bold")).pack(pady=10)
        self.final_score = tk.Label(self.end_frame, text="", font=
("Arial", 14))
        self.final_score.pack(pady=10)
        self.restart_button = tk.Button(self.end_frame, text="Play Again",
font=("Arial", 12, "bold"),
bg="#48bb78", fg="black", padx=20,
pady=10,
command=self.start_game)
        self.restart_button.pack(pady=10)
        tk.Label(self.end_frame, text="Problem History:", font=("Arial",
12, "bold")).pack(pady=5)
        self.history_frame = tk.Frame(self.end_frame, bd=1,
relief=tk.SOLID)
        self.history_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.canvas = tk.Canvas(self.history_frame, height=150)
        self.scrollbar = tk.Scrollbar(self.history_frame,
orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
"<Configure>",
lambda e:
self.canvas.configure(scrollregion=self.canvas.bbox("all"))
)
        self.canvas.create_window((0, 0), window=self.scrollable_frame,
anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def generate_math_problem(self, min_value, max_value):
        for i in range(1):
            operation_type = random.choice(['add', 'subtract', 'multiply',
'divide'])
            if operation_type == 'add':
                num1 = random.randint(min_value, max_value)
                num2 = random.randint(min_value, max_value)
                answer = num1 + num2
                problem_text = f"{num1} + {num2}"
            elif operation_type == 'subtract':
                num1 = random.randint(min_value, max_value)
                num2 = random.randint(min_value, max_value)
                if num1 < num2:
                    num1, num2 = num2, num1
                answer = num1 - num2
                problem_text = f"{num1} - {num2}"
            elif operation_type == 'multiply':
                num1 = random.randint(2, 12)
                num2 = random.randint(min_value, max_value)
                answer = num1 * num2
                problem_text = f"{num1} × {num2}"
            else:
                num2 = random.randint(2, 12)
                answer = random.randint(min_value, max_value)
                num1 = num2 * answer
                problem_text = f"{num1} ÷ {num2}"
        return {
'problem': problem_text,
'answer': answer
}

    def start_game(self):
        self.start_frame.pack_forget()
        self.end_frame.pack_forget()
        self.game_frame.pack(fill=tk.BOTH, expand=True)
        self.problems_list = []
        self.current_problem_index = 0
        self.score = 0
        self.time_left = 30
        self.score_display.config(text=f"Score: {self.score}")
        self.problem_counter.config(text=f"Problem: {self.current_problem_index + 1}")
        self.progress_bar.place(relwidth=1, relheight=1)
        self.feedback_message.config(text="")
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.get_new_problem()
        self.timer_running = True
        self.update_timer()
        self.answer_entry.focus_set()

    def get_new_problem(self):
        self.current_problem = self.generate_math_problem(2, 100)
        self.problem_display.config(text=f" {self.current_problem['problem']} = ?")
        self.answer_var.set("")
        self.answer_entry.focus_set()

    def check_answer_on_change(self, *args):
        if self.timer_running and self.current_problem:
            user_answer = self.answer_var.get().strip()
            if user_answer:
                try:
                    self.validate_and_process_answer(user_answer, True)
                except ValueError:
                    pass

    def validate_and_process_answer(self, user_answer, is_auto_check=False):
        if not self.timer_running or not self.current_problem or not user_answer:
            return
        try:
            numeric_answer = int(user_answer)
            is_correct = numeric_answer == self.current_problem['answer']
            if is_auto_check and not is_correct:
                return
            self.problems_list.append({
'problem': self.current_problem['problem'],
'correct_answer': self.current_problem['answer'],
'user_answer': user_answer,
'is_correct': is_correct
})
            if is_correct:
                self.score += 1
                self.score_display.config(text=f"Score: {self.score}")
                self.feedback_message.config(text="Correct!")
                self.root.after(1000, lambda: self.feedback_message.config(text=""))
            self.current_problem_index += 1
            self.problem_counter.config(text=f"Problem: {self.current_problem_index + 1}")
            self.get_new_problem()
        except ValueError:
            pass

    def update_timer(self):
        if self.timer_running:
            self.time_left -= 1
            self.timer_display.config(text=f"Time: {self.time_left}s")
            progress_width = self.time_left / 30
            self.progress_bar.place(relwidth=progress_width, relheight=1)
            if self.time_left <= 0:
                self.end_game()
            else:
                self.root.after(1000, self.update_timer)

    def end_game(self):
        self.timer_running = False
        self.game_frame.pack_forget()
        self.end_frame.pack(fill=tk.BOTH, expand=True)
        self.final_score.config(text=f"You scored {self.score} out of {self.current_problem_index}")
        self.display_history()

    def display_history(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        for i, problem in enumerate(self.problems_list):
            bg_color = "#c6f6d5" if problem['is_correct'] else "#fecaca"
            text_color = "#166534" if problem['is_correct'] else "#991b1b"
            history_item = tk.Frame(self.scrollable_frame, bg=bg_color,
bd=1, relief=tk.SOLID)
            history_item.pack(fill=tk.X, pady=2)
            problem_text = f"{problem['problem']} = {problem['correct_answer']}"
            tk.Label(history_item, text=problem_text, bg=bg_color,
fg="#1f2937", font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=5,
pady=5)
            answer_text = f"Your answer: {problem['user_answer']} {'✓' if problem['is_correct'] else '✗'}"
            tk.Label(history_item, text=answer_text, bg=bg_color,
fg=text_color, font=("Arial", 10)).pack(anchor=tk.W, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
