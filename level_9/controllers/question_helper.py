
from .files import FileHandler

from typing import Any
import os

class QuestionsHelper():
    def __init__(self,file_handler: FileHandler):
        self._file_handler = file_handler
        self._total_questions = len(self._file_handler.questions)
        self._current_question: dict[str, Any] = {}
        self._current_question_index = 0
        
    @property
    def current_question_index(self) -> int:
        return self._current_question_index
    @current_question_index.setter
    def current_question_index(self, index: int):
        if 0 <= index < self.total_questions:
            self._current_question_index = index
        else:
            raise IndexError("Question index out of range.")
    @property
    def current_question(self) -> dict[str, Any]:
        questions = self._file_handler.questions
        self._current_question = questions[self._current_question_index]
        return self._current_question
    def procede(self) -> None:
        print()
        input("Next (Enter) ⏭️  ? ")
        self.clear_console()
        self._current_question_index += 1
    @staticmethod
    def clear_console() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def reset(self) -> None:
        self._current_question_index = 0
    def ask(self) -> str:
        question  = self.current_question.copy()
        answer = self.ask_question(question)
        return answer

    @staticmethod
    def ask_question(question: dict[str, Any]) -> str:
        print(f"Q: {question.get('question', 'No question found.')}")
        print()
        answer = input("Your answer: ")
        return answer
    @property
    def total_questions(self) -> int:
        return self._total_questions
    def get_unasked_questions(self):
        return [q for q in self._file_handler.questions if not q.get("is_asked", False)]
    
    
if __name__ == "__main__":
    fh = FileHandler()
    qh = QuestionsHelper(fh)
    print(qh.current_question)
    qh.procede()
    print(qh.current_question)
    # print(qh.get_question_by_number(2))
    # print(qh.get_question_by_number(5))
    # print(qh.get_question_by_number(0))
    # print(qh.get_question_by_number(10))
    # print(qh.get_question_by_number(-1))
    # print(qh.get_question_by_number(1))
    # print(qh.get_question_by_number(3))
    # print(qh.get_question_by_number(4))
    # print(qh.get_question_by_number(6))
    # print(qh.get_question_by_number(7))
    # print(qh.get_question_by_number(8))
    # print(qh.get_question_by_number(9))
    # print(qh.get_question_by_number(11))