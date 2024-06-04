# TASK 1 and Task2
#print("Lets create your shopping list. \n What items do you need to add?")
   
def add_items():
    print("Lets create your shopping list. \n What items do you need to add? \n (Type 'done' to exit or 'remove' to modify) ")
    shopping_list = []     
    
    
    while True:
        item = input("Enter item: ")
        
        if item.lower() == 'done':
            break
        elif item.lower() == 'remove':
            
       # elif item == shopping_list:
            shopping_list.pop()

        else:
            shopping_list.append(item)
            

    return shopping_list 

     
new_list = add_items()    
print(new_list)

# Task 3

def shopping_list_format():
    print("Here is your final list of items to get: ", new_list)

    return new_list

shopping_list_format()