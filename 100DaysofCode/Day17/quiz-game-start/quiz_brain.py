# Todo 1. Ask the question to the user
# Todo 2. Check if the user's answer is correct
# Todo 3. Check if it's the end of the quiz


class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # If question_number == question_list, will return False.

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # At the same time that it makes the question number starts with 1,
        # increasing 1 to the question number will show the next question in
        # the next time that the method will be called.
        user_answer = input(f"Q.{self.question_number}-{current_question.text} [T/F]: ")
        while user_answer.lower() not in "tf":
            user_answer = input("Wrong answer, type [T] or [F] only: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user, answer):
        if user[0].upper() == answer[0]:
            print("\33[36mRight.\33[0;0m")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}\n\n")
        else:
            print("\33[31mWrong.\33[0;0m")
            print(f"Your score is {self.score}/{self.question_number}\n\n")



