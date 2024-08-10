import logging
from tkinter import Tk, Label, Button, Radiobutton, Frame, LabelFrame, StringVar, IntVar, LEFT
from tkinter.font import Font, nametofont, BOLD, ITALIC

from base10 import Base10Frame
from base2 import Base2Frame
from setup_logging import setup_logging
from utilities import Window, NumberEntry, TITLE, WIDTH, HEIGHT, RESIZABLE


class Main(Window):
	def __init__(self) -> None:
		self.root = Tk()

		# Variables
		self.correct_score_variable_base2 = StringVar(value='0')
		self.incorrect_score_variable_base2 = StringVar(value='0')
		self.min_value_variable = StringVar(value='1')
		self.max_value_variable = StringVar(value='100')
		self.game_type_variable = IntVar(value=0)

		self.min_value = int(self.min_value_variable.get())
		self.max_value = int(self.max_value_variable.get())
		self.current_game_type = 0

		self.quiz_frame: LabelFrame = LabelFrame(self.root, text='Quiz')
		self.number_label = Label()

		self.base10_frame = Base10Frame(self.root, self.quiz_frame, self.min_value_variable, self.max_value_variable)
		self.base2_frame = Base2Frame(self.root, self.quiz_frame, self.min_value_variable, self.max_value_variable)
		self.base10_frame.reset()

	def setup_window(self) -> None:
		self.root.wm_title(TITLE)
		self.root.wm_geometry(f'{WIDTH}x{HEIGHT}')
		self.root.wm_resizable(*RESIZABLE)

	def setup_settings(self) -> None:
		# Fonts
		title_font: Font = nametofont('TkDefaultFont').copy()
		title_font.config(size=30, weight=BOLD)

		small_title_font: Font = nametofont('TkDefaultFont').copy()
		small_title_font.config(size=15, weight=BOLD)

		small_font: Font = nametofont('TkDefaultFont').copy()
		small_font.config(size=8, slant=ITALIC)

		small_button_font = nametofont('TkDefaultFont').copy()
		small_button_font.config(size=10)

		# UI
		settings_frame: LabelFrame = LabelFrame(self.root, text='Settings')
		settings_frame.pack(side=LEFT, expand=True)

		# Game type
		Label(settings_frame, text='Game Type', font=title_font).pack()

		Radiobutton(settings_frame, text='Base 10 → Base 2', variable=self.game_type_variable, value=0,
		            command=self.switch_game_types).pack()
		Radiobutton(settings_frame, text='Base 2 → Base 10', variable=self.game_type_variable, value=1,
		            command=self.switch_game_types).pack()

		# Range
		Label(settings_frame, text='Range', font=title_font).pack(pady=(20, 0))

		range_frame: Frame = Frame(settings_frame)
		range_frame.pack()
		min_frame: Frame = Frame(range_frame)
		min_frame.pack(side=LEFT, padx=5)
		max_frame: Frame = Frame(range_frame)
		max_frame.pack(side=LEFT, padx=5)

		Label(min_frame, text='Min', font=small_title_font).pack(pady=3)
		NumberEntry(min_frame, width=7, textvariable=self.min_value_variable).pack(pady=3)
		Label(max_frame, text='Max', font=small_title_font).pack(pady=3)
		NumberEntry(max_frame, width=7, textvariable=self.max_value_variable).pack(pady=3)

		Label(settings_frame, text='After changing the range, the score will be automatically reset*',
		      font=small_font).pack()

		# Reset score
		Label(settings_frame, text='Score', font=title_font).pack(pady=(20, 0))
		Button(settings_frame, text='Reset Score', command=self.reset_score).pack(pady=7)

	def reset_score(self) -> None:
		self.base10_frame.correct_score_variable.set('0')
		self.base10_frame.incorrect_score_variable.set('0')
		self.base10_frame.total_score_variable.set('0')
		self.base2_frame.correct_score_variable.set('0')
		self.base2_frame.incorrect_score_variable.set('0')
		self.base2_frame.total_score_variable.set('0')

	def update_range_values(self, min_value: int, max_value: int) -> None:
		self.min_value_variable.set(str(min_value))
		self.max_value_variable.set(str(max_value))

	def switch_game_types(self) -> None:
		if self.current_game_type != self.game_type_variable.get():
			if self.game_type_variable.get() == 0:
				self.base10_frame.reset()
			else:
				self.base2_frame.reset()

			self.current_game_type = self.game_type_variable.get()

	def run(self) -> None:
		self.setup_window()
		self.setup_settings()
		self.root.mainloop()


# Main entry point
def main() -> None:
	# Setup logging
	setup_logging(level=logging.INFO, logging_format='[%(levelname)s]: %(message)s')

	# Run the app
	app: Main = Main()
	app.run()


if __name__ == '__main__':
	main()
