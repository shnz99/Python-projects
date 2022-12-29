from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125, text="Question text.", font=FONT, width="280"
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        ######################################## LABEL #############################################
        self.score_label = Label(
            text=f"Score: 0", fg="#fff", padx=20, pady=20, bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)

        ####################################### BUTTONS #############################################
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(
            text="",
            command=self.true_pressed,
            image=true_img,
            padx=20,
            pady=20,
            highlightthickness=0,
        )

        false_img = PhotoImage(file="images/false.png")
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(
            text="",
            command=self.false_pressed,
            image=false_img,
            padx=20,
            pady=20,
            highlightthickness=0,
        )
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")

        self.window.after(
            1000,
            self.get_next_question,
        )
