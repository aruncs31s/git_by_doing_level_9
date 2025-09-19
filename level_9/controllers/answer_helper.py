from .files import FileHandler
from .question_helper import QuestionsHelper
from typing import Any
import hashlib

class AnswersHelper:
    def __init__(self,file_handler: FileHandler ,question_helper: QuestionsHelper):
        self._file_handler = file_handler
        self.question_helper = question_helper
        self.current_ans: str = ""
        self.answers = self._file_handler.answers
        
    def check_answer(self) -> bool:
        question = self.question_helper.current_question
        return self._file_handler.check_answer_by_question(question, self.current_ans)
    
    def check_answer_by_question(self, question: dict[str, Any], answer: str) -> bool:
        answers = self.answers
        answer = answer.lower()
        """ convert it to sha256 """
        answer = hashlib.sha256(answer.encode()).hexdigest()
        for ans in answers:
            if ans.get("id", 0) == question.get("id", 0):
                correct_answers = [a.lower() for a in ans.get("answers", [])]
                user_answer = answer.lower()
                if user_answer == "":
                    return False
                if user_answer in correct_answers:
                    return True
        return False
