# Task 1

def fitness_tracker():

    activities = ["Dancing", "Biking", "Swimming", "Running"]
    duration = [10, 15, 20, 30]

    activity_input = input("What activity are you going to perform today?: ")

    if activity_input in activities:
        index = activities.index(activity_input)
        print(f"The duration of this workout is: {duration[index]} minutes.")
    else:
        print("The activity is not on the list.")
       

fitness_tracker()