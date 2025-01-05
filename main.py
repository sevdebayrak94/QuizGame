from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    next_question = Question(question_text,question_answer)
    question_bank.append(next_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()
print(f"You completed quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
