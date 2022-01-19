# Todo 1. Write a loop to iterate over question_data.
# Todo 2. Create a Question object from each entry in question_data.
# Todo 3. Append each Question object to the question bank.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    # You're iterating over question data dictionary
    question_text = item["text"]
    question_answer = item["answer"]
    # You're spliting texts and answers apart inside two variables
    new_question = Question(q_text=question_text, q_answer=question_answer)
    # Now you are  ↑calling↑ a Class and passing texts and answers through it
    question_bank.append(new_question)
    # You are appending texts and answers grouped as objects inside this list.
quiz = QuizBrain(question_bank)
# Finally, you're sending that list of objects to the QuizBrain in order to enumerate
# and keep each one in the quiz variable.
while quiz.still_has_questions():
    quiz.next_question()
# Now, the question will be printed with the number received.
if not quiz.still_has_questions():
    print(f"You've completed the Quiz.\n"
          f"Your final score is {quiz.score}")

# This is not that hard. Think calmly and you will understand.
# After all, are you or not 2% of the smartests?

