# Task 1

def quiz():
    print("Let's take a quiz, here are the questions:\n") 
    questions = [
        "What is the capital of Florida?",
        "What is the largest planet in our solar system?",
        "What is the currency of Japan?"
    ]

    answers = ["Tallahassee", "Jupiter", "Yen"]
    user_answers = []

    

    for question in questions:
        user_answer = input(question + " ")
        user_answers.append(user_answer)

    score = 0

    for i in range(len(questions)):
        if user_answers[i].lower() == answers[i].lower():
            print(f"Question {i+1}: Correct!")
            score += 1
        else:
            print(f"Question {i+1}: Wrong! The correct answer is {answers[i]}.")
    
    
    print(f"\nYou got {score} out of {len(questions)} correct.")

   
quiz()