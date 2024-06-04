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
print("This items are on your shopping list are: ", new_list)


