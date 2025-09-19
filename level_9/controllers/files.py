import json
from typing import TYPE_CHECKING, Any

data_path = 'data.json'
questions_path = 'questions.json'
answers_path = 'answers.json'
class FileHandler():
    def __init__(self):
        self._data_path: str = data_path
        self._questions_path: str = questions_path
        self._answers_path: str = answers_path
        self._datas: dict[str, Any] = {}
        self.all_questions: list[dict[str, Any]] = [{}]
        self._all_attempts: int = 0
        
        
    def get_data(self) -> dict[str, Any]:
        if self.datas == {}:
            data = self._load_json_file(self.data_path)
            self._datas = data
            return data
        else:
            return self.datas    
    @property
    def datas(self) -> dict[str, Any]:
        if self._datas == {}:
            datas = self._load_json_file(self.data_path)
            self._datas = datas
        return self._datas
    @datas.setter
    def datas(self, value: dict[str, Any]):
        self._datas = value
        
    @property
    def all_attempts(self) -> int:
        if  self._all_attempts == 0:
            data = self._data()
            _all_attempts = data.get("status", {}).get("attempts", 0)
            if not isinstance(_all_attempts, int):
                _all_attempts = 0
            self._all_attempts = _all_attempts
        return self._all_attempts
    @all_attempts.setter
    def all_attempts(self, value: int):
        # May Be used to reset attempts
        self._all_attempts = value
        self.save_attempts(value)

    def _get_file_paths(self, filename: str) -> list[str]:
        """Helper method to get possible file paths"""
        return [
            f"{filename}",
            f"level_9/{filename}"
        ]
    
    def _load_json_file(self, filename: str) -> dict[str, Any]:
        """Helper method to load JSON file with fallback paths"""
        paths = self._get_file_paths(filename)
        try:
            with open(paths[0], 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            with open(paths[1], 'r') as file:
                return json.load(file)
    @property
    def data_path(self) -> str:
        return self._data_path
    @data_path.setter
    def data_path(self, path: str) -> None:
        self._data_path = path

    @property
    def questions_path(self):
        return self._questions_path
    @questions_path.setter
    def questions_path(self, path: str):
        self._questions_path = path
    
    
    
    @property
    def questions(self) -> list[dict[str, Any]]:
        return self._questions()
    def _questions(self) -> list[dict[str, Any]]:
        if len(self.all_questions) == 0 or self.all_questions == [{}]:
            questions = self._load_json_file(self.questions_path)
            self.all_questions = questions['questions']
            return questions['questions']
        else:
            return self.all_questions
    def _data(self) -> dict[str, Any]:
        if self.datas == {}:
            data = self._load_json_file(self.data_path)
            self.datas = data 
            return self.datas
        else:
            return self.datas
    @property
    def attempts(self) -> int:
        if self.all_attempts == 0:
            data = self._data()
            self.all_attempts = data.get("status", {}).get("attempts", 0)
        return self.all_attempts
    
    def save_attempts(self, attempts: int) -> None:
        data = self._data()
        data["status"]["attempts"] = attempts
        self.save_data(data)


    def _save_data(self, data: dict[str, Any]) -> bool:
        try:
            with open(self.data_path, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
        self.datas = data
        return True

    def _save_questions(self, questions: list[dict[str, Any]]) -> bool:
        try:
            with open(self.questions_path, 'w') as file:
                json.dump({"questions": questions}, file)
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
        return True

    def save_status(self, questions: list[dict[str, Any]], is_finished: bool, current_question: int, attempts: int) -> bool:
        """Save the current status including progress on questions"""
        try:
            data = self._data()
            
            # Update status with current question progress
            if not data.get("status"):
                data["status"] = {
                    "is_completed": is_finished,
                    "current_question": current_question,
                    "attempts": attempts,
                }
            else:
                data["status"]["is_completed"] = is_finished
                data["status"]["current_question"] = current_question
                data["status"]["attempts"] = attempts
            self._save_questions(questions)
            self._save_data(data)
            return True
        except Exception as e:
            print(f"Error saving status: {e}")
            return False
 
                    

    def get_current_question_index(self) -> int:
        data = self._data()
        return data.get("status", {}).get("current_question", 0)
    def played_before(self) -> bool:
        data = self._data()
        status = data.get("status", {})
        return status.get("attempts", 0) > 0
    """ Answers """
    @property
    def answers(self) -> list[dict[str, Any]]:
        answers = self._answers()
        return answers

    def _answers(self) -> list[dict[str, Any]]:
        answers = self._load_json_file(self._answers_path)
        return answers.get("answers", [])

   
if __name__ == "__main__":
    fh = FileHandler()
    print(fh.datas)
    print(fh.questions)
    print(fh.answers)
    # print(fh.attempts)
    # print(fh.all_attempts)
    # fh.save_attempts(5)
    # print(fh.attempts)
    # print(fh.all_attempts)
    # print(fh.get_current_question_index())
    # print(fh.played_before())
    # q = fh.questions[0]
    # fh.update_question_status(q, True)
    # print(fh.questions)