# Task 1

def fitness_tracker():

    activities = ["Dancing", "Biking", "Swimming", "Running"]
    durations = [10, 15, 20, 30]

    activity_input = input("What activity are you going to perform today?: ").lower()
    activities_lower = [activity.lower() for activity in activities]
    
    if activity_input in activities_lower:
        index = activities_lower.index(activity_input)
        print(f"The duration of this workout is: {durations[index]} minutes.")
    else:
        print("The activity is not on the list.")
       

fitness_tracker()

# Task 2 and Task 3

def calories_burned():
    activities = ["Dancing", "Biking", "Swimming", "Running"]
    durations = [10, 15, 20, 30]
    

    activity_input = input("What activity are you going to perform today so we can calculate the calories burned?: ").lower()
    activities_lower = [activity.lower() for activity in activities]
    
    if activity_input in activities_lower:
        index = activities_lower.index(activity_input)
        duration = durations[index]
        calories_calc = duration * 3.5

        print(f"The activity you chose was: {activities[index]} \n The duration of this workout is: {durations[index]} minutes. \n You burned {calories_calc} calories.")
    else:
        print("The activity is not on the list.")

calories_burned()