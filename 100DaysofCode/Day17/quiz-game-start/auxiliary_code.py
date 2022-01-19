# num_questions = len(question_bank)
# answered_questions = 0
# order = sorted(range(0, num_questions))
# score = 0
# counter = 1
# while not answered_questions == num_questions:
#     pick_question = random.choice(order)
#     print(f"QUESTION{counter}: {question_bank[pick_question].text}")
#     answer = input("\33[31m[T]\33[0;0mrue\n"
#                    "\33[31m[F]\33[0;0malse\n"
#                    "Your choice: ")
#     while answer.lower() not in "tf":
#         answer = input("Wrong answer, type [T] or [F] only: ")
#     if answer.upper() == question_bank[pick_question].answer[0]:
#         print("\33[36mRight.\33[0;0m")
#         score += 1
#         order.remove(pick_question)
#         answered_questions += 1
#         counter += 1
#     else:
#         print("\33[31mWrong.\33[0;0m")
#         order.remove(pick_question)
#         answered_questions += 1
#         counter += 1
#     print(f"Score: {score}")
#     if answered_questions == num_questions:
#         print(f"You finished the quizz.\n"
#               f"You scored {score}.")
#         if score == 12:
#             print(f"That's SPETACULAR!!")
#         elif score >= 9:
#             print(f"That's awesome!")
#         elif score >= 6:
#             print(f"Nice result")
#         elif score < 4:
#             print(f"That's very low")
