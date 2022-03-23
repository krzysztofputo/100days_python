from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for data in question_data:
    question = data["text"]
    answer = data["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

