import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randrange, shuffle
from tkinter import Tk, StringVar, Entry, Frame, CENTER
from typing import List, Dict, Tuple, Final, Any, Unpack

# Window
TITLE: Final[str] = 'BinarY'
WIDTH: Final[int] = 580
HEIGHT: Final[int] = 380
RESIZABLE: Final[Tuple[bool, bool]] = False, False

# Colors
RED: Final[str] = '#FF0200'
GREEN: Final[str] = '#69FF00'


# Dataclasses
@dataclass(frozen=True, order=True)
class Question:
	number: int
	answers: List[str]
	correct_answer: str


# Functions
def generate_question_base10(min_value: int, max_value: int) -> Question:
	correct_number: int = randrange(min_value, max_value)
	correct_answer: str = bin(correct_number)[2:]
	answers: List[str] = [bin(randrange(min_value, max_value))[2:] for _ in range(3)] + [correct_answer]
	shuffle(answers)

	return Question(number=correct_number, answers=answers, correct_answer=correct_answer)


def generate_question_base2(min_value: int, max_value: int) -> Question:
	correct_number: int = bin(randrange(min_value, max_value))[2:]
	correct_answer: str = int(f'0b{correct_number}', 2)
	answers: List[str] = [randrange(min_value, max_value) for _ in range(3)] + [correct_answer]
	shuffle(answers)

	return Question(number=correct_number, answers=answers, correct_answer=correct_answer)


# Classes
class Window(ABC):
	@abstractmethod
	def __init__(self) -> None:
		pass

	@abstractmethod
	def setup_window(self) -> None:
		pass

	@abstractmethod
	def run(self) -> None:
		pass


class QuizFrame(ABC):
	@abstractmethod
	def __init__(self, root: Tk, frame: Frame, min_value_variable: StringVar, max_value_variable) -> None:
		pass

	@abstractmethod
	def setup_quiz(self) -> None:
		pass

	@abstractmethod
	def verify_result(self, text: str) -> None:
		pass

	@abstractmethod
	def get_range_values(self) -> None:
		pass

	@abstractmethod
	def reset(self) -> None:
		pass

	@abstractmethod
	def update_range_values(self, min_value: int, max_value: int) -> None:
		pass

	@abstractmethod
	def reset_score(self) -> None:
		pass

	@abstractmethod
	def clear_quiz_frame(self) -> None:
		pass


class NumberEntry(Entry):
	def __init__(self, master: Any, **kwargs: Unpack[Dict[str, Any]]) -> None:
		super().__init__(master, **kwargs)
		self.configure(justify=CENTER, validate='key', validatecommand=(self.register(self.on_validate), '%P'))

	@staticmethod
	def on_validate(new_value: str) -> bool:
		return new_value == '' or re.match(r'^\d*$', new_value) is not None


if __name__ == '__main__':
	print(generate_question_base2(1, 100))
