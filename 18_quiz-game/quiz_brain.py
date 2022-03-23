from data import question_data
from question_model import Question

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        while self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number+=1
            print(f"Q{self.question_number} {current_question.question} (True/False): ")
            answer = input().capitalize()
            if current_question.answer == answer:
                self.score += 1
                print(f"You're correct! {self.score}/{self.question_number}")
            else:
                print(f"That's wrong {self.score}/{self.question_number}")
        print(f"Your final score was {self.score}/{self.question_number}")




