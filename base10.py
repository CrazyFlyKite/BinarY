from tkinter import Tk, Label, Button, Frame, StringVar, LEFT
from tkinter.font import Font, nametofont, BOLD
from tkinter.messagebox import showerror

from utilities import QuizFrame, generate_question_base10, RED, GREEN


class Base10Frame(QuizFrame):
	def __init__(self, root: Tk, frame: Frame, min_value_variable: StringVar, max_value_variable: StringVar) -> None:
		self.root = root

		# Variables
		self.correct_score_variable = StringVar(value='0')
		self.incorrect_score_variable = StringVar(value='0')
		self.total_score_variable = StringVar(value='0')
		self.min_value_variable = min_value_variable
		self.max_value_variable = max_value_variable

		self.current_question = generate_question_base10(1, 100)
		self.min_value = int(self.min_value_variable.get())
		self.max_value = int(self.max_value_variable.get())

		self.quiz_frame = frame
		self.number_label = Label()

	def setup_quiz(self) -> None:
		# Fonts
		title_font: Font = nametofont('TkDefaultFont').copy()
		title_font.config(size=30, weight=BOLD)

		subtitle_font_font: Font = nametofont('TkDefaultFont').copy()
		subtitle_font_font.config(size=20)

		# UI
		self.quiz_frame.pack(side=LEFT, expand=True)

		# Question
		Label(self.quiz_frame, text='Base 10:', font=subtitle_font_font).pack(pady=5)
		self.number_label = Label(self.quiz_frame, text=str(self.current_question.number), font=title_font)
		self.number_label.pack()

		# Buttons
		Label(self.quiz_frame, text='Base 2:', font=subtitle_font_font).pack(pady=5)

		buttons_frame: Frame = Frame(self.quiz_frame)
		buttons_frame.pack(pady=7)

		index: int = 0
		for i in range(2):
			for j in range(2):
				text: str = self.current_question.answers[index]
				Button(buttons_frame, text=text, width=10, command=lambda t=text: self.verify_result(t)).grid(row=i,
				                                                                                              column=j)
				index += 1

		Button(self.quiz_frame, text='Reset', command=self.reset).pack(pady=(50, 0))

		# Score
		score_frame: Frame = Frame(self.quiz_frame)
		score_frame.pack(pady=(5, 20))

		Label(score_frame, foreground=GREEN, textvariable=self.correct_score_variable, width=3,
		      font=title_font).pack(side=LEFT, padx=10, expand=True)
		Label(score_frame, textvariable=self.total_score_variable, width=3).pack(side=LEFT, padx=10, expand=True)
		Label(score_frame, foreground=RED, textvariable=self.incorrect_score_variable, width=3,
		      font=title_font).pack(side=LEFT, padx=10, expand=True)

	def verify_result(self, text: str) -> None:
		if text == self.current_question.correct_answer:
			self.correct_score_variable.set(str(int(self.correct_score_variable.get()) + 1))
		else:
			self.incorrect_score_variable.set(str(int(self.incorrect_score_variable.get()) + 1))

		self.total_score_variable.set(str(int(self.total_score_variable.get()) + 1))
		self.reset()

	def get_range_values(self) -> None:
		min_value, max_value = self.min_value_variable.get(), self.max_value_variable.get()

		if not (min_value and max_value):
			showerror('Value Error', 'Please, enter the correct values for min and max values!')
			return

		min_value, max_value = int(min_value), int(max_value)

		if min_value > max_value:
			min_value, max_value = max_value, min_value
			self.update_range_values(min_value, max_value)
		elif min_value == max_value:
			max_value = min_value + 10
			self.update_range_values(min_value, max_value)

		if max_value > 10_000:
			max_value = 10_000
			self.update_range_values(min_value, max_value)

		if min_value != self.min_value or max_value != self.max_value:
			self.reset_score()

		self.min_value, self.max_value = int(min_value), int(max_value)

	def reset(self) -> None:
		self.get_range_values()
		self.current_question = generate_question_base10(self.min_value, self.max_value)
		self.clear_quiz_frame()
		self.setup_quiz()

	def update_range_values(self, min_value: int, max_value: int) -> None:
		self.min_value_variable.set(str(min_value))
		self.max_value_variable.set(str(max_value))

	def reset_score(self) -> None:
		self.correct_score_variable.set('0')
		self.incorrect_score_variable.set('0')
		self.total_score_variable.set('0')

	def clear_quiz_frame(self) -> None:
		for widget in self.quiz_frame.winfo_children():
			widget.destroy()
