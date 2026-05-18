import tkinter as tk
import turtle
from survey import get_question, get_answer_options, save_answers
from counting import results

# constants
question_file = "questions.txt"
answer_options_file = "answer_options.csv"
answer_file = "responses.txt"

question_list = get_question(question_file)
answer_options_list = get_answer_options(answer_options_file)


class Display:
    def __init__(self):
        self.current_question = 0
        self.root = tk.Tk()
        self.init_window()
        self.create_interface_frame()
        self.create_turtle_frame()
        self.create_turtle_canvas()
        self.create_buttons()

    # creating the screen
    def init_window(self):
        self.root.title("The Adventures of the Turtle")
        self.screen_size = (1100, 700)
        self.root.geometry(f"{self.screen_size[0]}x{self.screen_size[1]}")

    # creating the bottom panel for the buttons and to display the questions
    def create_interface_frame(self):
        self.interface_frame = tk.Frame(
            self.root, width=800, height=(0.25 * self.screen_size[1])
        )
        self.interface_frame.grid(row = 1, column = 0, )

    # creating buttons + setting their dimensions and font
    def create_buttons(self):
        self.text = tk.Label(
            self.interface_frame,
            text=question_list[self.current_question],
            font="Garamond 12",
            wraplength = 750,
            justify = "center",
            anchor = "center"
        )
        self.text.grid(row=0, column =0, columnspan=3, sticky="ew", pady=(10, 5))

        # setup of button to move turtle left
        self.a = tk.Button(
            self.interface_frame,
            text=answer_options_list[self.current_question][0],
            font="Garamond 12",
            wraplength = 200,
            justify = "center",
            width=30,
            height=5,
            command=self.move_left,
        )
        self.a.grid(row=1, column=0, sticky="ew", padx=10)

        # setup of button to move turtle forward
        self.b = tk.Button(
            self.interface_frame,
            text=answer_options_list[self.current_question][1],
            font="Garamond 12",
            wraplength = 200,
            justify = "center",
            width=30,
            height=5,
            command=self.move_forward,
        )
        self.b.grid(row=1, column=1, sticky="ew", padx=10)

        # setup of button to move turtle right
        self.c = tk.Button(
            self.interface_frame,
            text=answer_options_list[self.current_question][2],
            font="Garamond 12",
            wraplength = 200,
            justify = "center",
            width=30,
            height=5,
            command=self.move_right,
        )
        self.c.grid(row=1, column=2, sticky="ew", padx=10)

    # frame for the turtle canvas to be created
    def create_turtle_frame(self):
        self.turtle_frame_height = int(0.75 * self.screen_size[1])
        self.turtle_frame_width = int(self.screen_size[0])
        self.turtle_frame = tk.Frame(
            self.root,
            width=self.turtle_frame_width,
            height=self.turtle_frame_height,
        )

        self.turtle_frame.grid(row=0, column=0)

    # map that the turtle runs on + turtle
    def create_turtle_canvas(self):
        self.action_canvas = tk.Canvas(
            self.turtle_frame,
            width=800,
            height=500,
        )
        self.action_canvas.pack()
        self.turtle_screen = turtle.TurtleScreen(self.action_canvas)
        self.turtle_screen.bgcolor("DarkGreen")
        self.t = turtle.RawTurtle(self.turtle_screen)

        self.t.setheading(90)
        self.t.penup()
        self.t.setpos(0, -0.4 * (self.action_canvas.winfo_height()))

    # showing the next questions + answer options, or calculating the final results
    def next_question(self):
        self.current_question += 1
        if self.current_question < len(question_list):
            self.text.config(text = question_list[self.current_question])
            self.a.config(text = answer_options_list[self.current_question][0])
            self.b.config(text = answer_options_list[self.current_question][1])
            self.c.config(text = answer_options_list[self.current_question][2])
        else:
            self.a.grid_remove()
            self.b.grid_remove()
            self.c.grid_remove()
            self.text.config(text = results())

    # assigns button to have turtle move left
    def move_left(self):
        self.t.left(90)
        self.t.forward(75)
        self.t.right(90)
        save_answers("A")
        self.next_question()

    # assigns button to have turtle move right
    def move_right(self):
        self.t.right(90)
        self.t.forward(75)
        self.t.left(90)
        save_answers("C")
        self.next_question()

    # assigns button to have turtle move forward
    def move_forward(self):
        self.t.forward(75)
        save_answers("B")
        self.next_question()