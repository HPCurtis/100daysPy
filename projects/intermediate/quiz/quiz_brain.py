class QuizBrain:
    def __init__(self, question_l):
        self.question_number = 0
        self.question_list = question_l
        self.score = 0

    def check_ans(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are correct")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
        else: 
            print("You are incorrect")
            print(f"The correct answer was {correct_answer}")
            print(f"Your current score is {self.score}/{self.question_number}")
    

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):

        while self.still_has_questions():
            question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
            self.check_ans(user_answer, question.answer)
