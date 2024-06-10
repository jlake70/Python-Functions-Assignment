# Task 1

def quiz():
    print("Lets take a quiz, here are the questions: ") 
    questions = ["Question 1: What is the capital of Florida? \n ",
                "Question 2: What is the largest planet in our solar system? \n",
                "Question 3: What is the currency of Japan?\n"]
    
    answers = ["Tallahassee", "Jupiter", "Yen"]

    score = 0
    
    #while True:
    for i in range(len(questions)):
            user_answers = input(questions[i] + " ")

    if user_answers.lower() == answers[0].lower():
            print("You got it right!")

            score += 1
    
    elif user_answers.lower() == answers[1].lower():
            print("You got it right!")
            score += 1

     
    elif user_answers.lower() == answers[2].lower():
            print("You got it right!")
            score += 1
            print(f"You got {score} out of {len(questions)} correct.") 
          
    else:
            print(f"Wrong! The correct answer is {answers[0]}, {answers[1]}, {answers[2]} .") 

            
        

quiz()
