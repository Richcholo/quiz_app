# TODO: ADD USER INTERFACE
# TODO: INTEGRATE QUIZ CLASS WITH UI
# Notes from bon: Palitan nyo nalang ung kulay nung UI alam nyo namang minalas ako sa mata

import tkinter as tk
from tkinter import ttk
from quiz import Quiz 

#question screen
def question(root):
    
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#1e1e2f")

    # score
    score_label = tk.Label(
        root,
        text="Score: 0",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#1e1e2f"
    )
    score_label.place(x=1050, y=90)

    # questions
    question_label = tk.Label(
        root,
        text="Question 1:",
        font=("Arial", 22, "bold"),
        fg="white",
        bg="#1e1e2f"
    )
    question_label.pack(pady=30)

    # Frame for multiple choice buttons
    mc_frame = tk.Frame(root, bg="#4A4A4A", padx=40, pady=30)
    mc_frame.pack(pady=20)

    # Placeholder choices
    choices = ["A. A", "B. B", "C. C", "D. D"]

    for choice in choices:
        tk.Button(
            mc_frame,
            text=choice,
            font=("Arial", 16, "bold"),
            width=20,
            height=1,
            bg="#4a4ad9",
            fg="white",
            relief="flat",
            activebackground="#3838d1"
        ).pack(pady=10)

#main screen
def load_screen(root):
   
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(background="#1e1e2f")

    # title natin
    title = tk.Label(
        root,
        text="Choose a Quiz Topic",
        font=("Arial", 26, "bold"),
        fg="white",
        bg="#1e1e2f"
    )
    title.pack(pady=30)

    # ung box around the button
    btn_frame = tk.Frame(root, bg="#4A4A4A", padx=40, pady=30)
    btn_frame.pack(pady=20)

    topics = ["Gaming", "Music", "IT Questions"]

    for topic in topics:
        tk.Button(
            btn_frame,
            text=topic,
            font=("Arial", 16, "bold"),
            width=18,
            height=2,
            bg="#4a4ad9",
            fg="white",
            relief="flat",
            activebackground="#3838d1",
            command=lambda t=topic: question(root)   # switch screen
        ).pack(pady=12)


def main():

    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("600x430")
    root.configure(background="#1e1e2f")

    load_screen(root)

    root.mainloop()


if __name__ == "__main__":
    main()
