from .files import FileHandler
from .question_helper import QuestionsHelper
from .answer_helper import AnswersHelper
import os
class QuizController:
    def __init__(self,
                file_handler: FileHandler ,
                question_helper: QuestionsHelper,
                answer_helper: AnswersHelper,
                ):
        self.file_handler = file_handler
        self.question_helper = question_helper
        self.answer_helper = answer_helper
        
        self.attempts = self.file_handler.all_attempts
        self.current_question_index = 0
        self.is_finished = False
        
    def _is_played_before(self) -> bool:
        data = self.file_handler.get_data()
        status = data.get("status", {})
        return status.get("attempts", 0) > 0
    def intro(self):
        self.question_helper.clear_console()
        print("  Welcome to the Quiz!".center(50, "="))
        print("  level 9  ".center(50, "="))
    def initialize(self):
        if self.attempts == 0:
            self.intro()
        if self._is_played_before():
            self.current_question_index = self.file_handler.get_current_question_index()
            self.question_helper.current_question_index = self.current_question_index
            self.question_helper.clear_console()
            print("Welcome back!")
        # Get unasked questions 
        else:
            self.current_question_index = 0
        unasked_questions = self.question_helper.get_unasked_questions()
        if len(unasked_questions) == 0:
            print("You have already completed this level.")
            self.is_finished = True
            if (self.is_finished):
                # TODO: Show status here also
                print("Quiz Finished!")
            return 
        if self.is_finished:
            if self.attempts == 0:
                print("error: No attempts made but quiz already finished?. Report it to admins")
                return
            print("Quiz already finished.")
            return
        if self.question_helper.total_questions == 0:
            print("No questions available.")
            return
    def start(self):
        # How to start the quiz
        '''
        - First check the number of questions 
        - Check if the player has already played it before 
        - if true , then check the number of questions he answered,
        - then check the number of correct answers
        - the interate through each question and ask him.
        - Last print the results.
        '''
        
        while not self.is_finished:
            self.progress()
            if self.current_question_index >= self.question_helper.total_questions:
                self.is_finished = True
                print("Quiz Finished! 🥳 ")
                
                return
            answer =self.question_helper.ask()
            if self.answer_helper.check_answer_by_question(self.question_helper.current_question, answer):
                print("Correct! ✅")
                self.question_helper.current_question["is_asked"] = True
                self.question_helper.current_question["is_correct"] = True
                self.question_helper.current_question["is_answered"] = True
                self.question_helper.procede()
                self.current_question_index += 1
                self.file_handler.save_status(
                    questions=self.file_handler.questions,
                    is_finished=self.is_finished,
                    current_question=self.current_question_index,
                    attempts=self.attempts + 1
                )  
            else:
                self.question_helper.clear_console()
                print(f"{answer} ❌ Is Incorrect. Try again.")
            

    def progress(self):
        print("Status:")
        print(f"Current Question: {self.current_question_index}")
        print(f"Total Questions: {self.question_helper.total_questions}")
        print()
        
