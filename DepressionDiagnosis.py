import tkinter as tk
from tkinter import messagebox

class DepressionDiagnosisGUI:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Depression Diagnosis System")
        master.geometry("600x300")
        master.resizable(False, False)

        # Note for the duration of 2 weeks
        self.duration_note_label = tk.Label(master, text="Please respond based on how you have been feeling over the last 2 weeks.")
        self.duration_note_label.pack(pady=(10, 10))

        # Knowledge Base
        self.symptoms = {
            # Symptom : Severity, weight
            "feeling down or hopeless most of the day": [None, 3],
            "Loss of interest or pleasure in activities ": [None, 3],
            "Significant change in appetite or weight ": [None, 2],
            "trouble sleeping too much or insomnia": [None, 2],
            "feeling slowed down or agitated": [None, 2],
            "Fatigue or low energy": [None, 2],
            "Feelings of worthlessness or guilt": [None, 2],
            "Difficulty thinking, concentrating, or making decisions": [None, 2],
            "Thoughts of death or suicide\n !!if present seek immediate help!!": [None, 4],
        }

        self.questions = list(self.symptoms.keys())
        self.current_question_index = 0

        self.question_label = tk.Label(master, text="")
        self.question_label.pack(pady=10)

        self.severity_var = tk.IntVar(value=-1)

        # Part of KB
        self.severity_options = {
            "All of the time": 5,
            "Most of the time": 4,
            "Half of the time": 3,
            "Some of the time": 2,
            "Not at all": 0
        }

        for text, value in self.severity_options.items():
            button = tk.Radiobutton(master, text=text, variable=self.severity_var, value=value)
            button.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(fill=tk.X)

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.previous_question)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_question)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=5)

        self.update_question()

    def update_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question)
        self.check_button_state()

    def check_button_state(self):
        if self.current_question_index == 0:
            self.prev_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL)
        if self.current_question_index == len(self.questions) - 1:
            self.next_button.config(text="Diagnose")
        else:
            self.next_button.config(text="Next")

    def next_question(self):
        question = self.questions[self.current_question_index]
        self.symptoms[question][0] = self.severity_var.get()
        self.severity_var.set(-1)  # Reset severity selection
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
        else:
            self.diagnose()
            self.reset_counter()  # Reset counter after diagnosis
        self.update_question()

    def previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
        self.update_question()

    def reset_counter(self):
        self.current_question_index = 0

    # Inference engine
    def diagnose(self):
        # Scoring logic
        score = sum(val[0] * val[1] for val in self.symptoms.values() if val[0] is not None)
        threshold1 = 50
        threshold2 = 30
        # Decision making logic
        if score >= threshold1:
            result = "High likelihood of depression."
        elif score >= threshold2:
            result = "Moderate likelihood of depression."
        else:
            result = "Low likelihood of depression."

        messagebox.showinfo("Diagnosis Result", result)

def main():
    root = tk.Tk()
    app = DepressionDiagnosisGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
