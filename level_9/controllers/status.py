
class Status():
    def __init__(self):
        self._is_finished = False
        self.current_question_index = 0
        self._attempts = 0
    @property
    def attempts(self) -> int:
        return self._attempts
    @attempts.setter
    def attempts(self, value: int):
        self._attempts = value

    @property
    def current_question(self):
        return self.current_question_index
    @current_question.setter
    def current_question(self, index: int):
        self.current_question_index = index
    @property
    def is_finished(self) -> bool:
        return self._is_finished
    @is_finished.setter
    def is_finished(self, value: bool):
        self._is_finished = value

    def progress(self):
        print("Status:")
        print(f"Current question: {self.current_question_index}")
        print(f"Is finished: {self.is_finished}")
    def played_before(self, file_handler) -> bool:
        data = file_handler.data()
        status = data.get("status", {})
        return status.get("attempts", 0) > 0
