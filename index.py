# Notes from bon: Palitan nyo nalang ung kulay nung UI alam nyo namang minalas ako sa mata
# TODO: Pagandahin yung UI, try natin maglagay ng progress bar sa ilalim or something.
# TODO: Change background colors, masyado siyang dark rn

import tkinter as tk
from quiz import Quiz 

BG_MAIN = "#0c0c25"     # changed
BG_FRAME = "#0c0c25"    # same as bg
BTN_MAIN = "#6c8ef5"
BTN_ACTIVE = "#5a7ae0"
TEXT_MAIN = "#ffffff"    # choose a topic white

# Screen that shows when quiz is done
def results_screen(root, quiz):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#0c0c25")

    tk.Label(
        root,
        text="Quiz Finished!",
        font=("Arial", 26, "bold"),
        fg="white",
        bg="#0c0c25"

    ).pack(pady=40)
        # Display Highscore for the current topic
    quiz.save_highscore()
    topic = quiz.current_topic
    highscore = quiz.get_highscore(topic)
    tk.Label(
        root,
        text=f"{topic} Highscore: {highscore}",
        font=("Arial", 20),
        fg="yellow",
        bg="#0c0c25"
    ).pack(pady=10)

    tk.Label(
        root,
        text=f"Your Final Score:\n{quiz.score} / 5",
        font=("Arial", 22, "bold"),
        fg="#4cd137", # Green color for score
        bg="#0c0c25"
    ).pack(pady=20)

    # Restart Button
    tk.Button(
        root,
        text="Play Again",
        font=("Arial", 16, "bold"),
        width=15,
        bg="#4a4ad9",
        fg="white",
        relief="flat",
        command=lambda: load_screen(root, quiz)
    ).pack(pady=20)

    # Exit Button
    tk.Button(
        root,
        text="Exit",
        font=("Arial", 14),
        width=10,
        bg="#d63031", # Red color
        fg="white",
        relief="flat",
        command=root.destroy
    ).pack(pady=5)

# Question screen
def question(root, quiz):
    
    # 1. Get data from quiz class FIRST
    q_text, options = quiz.get_question_data()

    # 2. Check if the quiz is actually over
    if q_text == "Quiz Finished":
        results_screen(root, quiz)
        return # Stop running this function

    # 3. If not over, clear screen and draw UI
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#0c0c25")

    # Score Label (Fixed f-string syntax)
    score_label = tk.Label(
        root,
        text=f"Score: {quiz.score}",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#0c0c25"
    )
    score_label.place(x=450, y=20)

    # Question Number Label (Dynamic: 1, 2, 3...)
    tk.Label(
        root,
        text=f"Question {quiz.q_index + 1}:", 
        font=("Arial", 14, "bold"),
        fg="#aaaaaa", # Grey color
        bg="#0c0c25"
    ).pack(pady=(30, 60))

    # The Question Text
    question_label = tk.Label(
        root,
        text=q_text,
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#0c0c25",
        wraplength=500,
        justify="center",
    )
    question_label.pack(pady=10)

    # Frame for multiple choice buttons
    mc_frame = tk.Frame(root, bg="#0c0c25", padx=40, pady=20)
    mc_frame.pack(pady=20)

    # Generate choices for buttons
    for choice in options:
        tk.Button(
            mc_frame,
            text=choice,
            font=("Arial", 12, "bold"),
            width=30,
            height=1,
            bg="#4a4ad9",
            fg="white",
            relief="flat",
            bd=0,
            activebackground="#3838d1",
            # Logic: Check answer, then reload this screen
            command=lambda c=choice: [quiz.check_answer(c), question(root, quiz)] 
        ).pack(pady=5)

    tk.Button(root, text="Back to Menu",font=("Arial", 12, "bold"), fg="white", bg="#d94a4a", relief="flat",
              command=lambda: load_screen(root, quiz)).pack(pady=10)


# Main screen
def load_screen(root, quiz):
   
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(background="#0c0c25")

    title = tk.Label(
        root,
        text="Choose a Quiz Topic",
        font=("Arial", 26, "bold"),
        fg="white",
        bg="#0c0c25"
    )
    title.pack(pady=(80,20))


    # Note: These names must match dictionary keys in quiz.py
    topics = ["Gaming", "Music", "IT Questions"]

    for topic in topics:
        tk.Button(
    
            text=topic,
            font=("Arial", 16, "bold"),
            width=20,
            height=2,
            bg="#4a4ad9",
            fg="white",
            relief="flat",
            activebackground="#3838d1",
            command=lambda t=topic: [quiz.start_topic(t), question(root, quiz)]
        ).pack(pady=12)


def main():
    quiz = Quiz()
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("600x550") # Increased height slightly
    root.configure(background="#0c0c25")

    load_screen(root, quiz)

    root.mainloop()


if __name__ == "__main__":
    main()
