from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

def main():
    qb = question_bank()
    quiz_brain = QuizBrain(question_l = qb)

    quiz_brain.next_question()
    print("You have finished the quiz")
    print(f"Your final socre was: {quiz_brain.score}/{quiz_brain.question_number}")

def question_bank():
    qb = []
    for data in question_data:
        question = Question(text = data["text"], answer = data["answer"])
        qb.append(question)
    
    return qb
        

if __name__ == "__main__":
    main()