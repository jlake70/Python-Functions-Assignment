# Task 1 and Task 2

def grade_average(grades):
    print("What are your grades?")
    #grades = input("Enter your Scores (0-100, type 'done' to finish): ")
    
    
    total = sum(grades)
    counter = len(grades)
    average = total / counter
    
    return average
    
    
grades = [91,89,96,99,76,67]

final_average = grade_average(grades)
print(f"Your average is : {final_average}")

highest = max(grades)
lowest = min(grades)
print(f"Your highest grades was: {highest}")
print(f"Your lowest grade was : {lowest}")

#Task 3

def letter_grade():
    grade = float(input("Enter your Average (0-100): "))

    if grade <=60:
        print("You got an F!")
    elif grade <=69:
        print("You got a D!")
    elif grade <=80:
        print("You got a C!")
    elif grade <=90:
        print("You got a B!")
    elif grade <=100:
        print("You got a A!")
    else:
        print("Let me know your score.")

letter_grade()
