""""
A dialog system for ordering Salad and Pizza.
"""

def select_meal():

    complete = None
    ordered = False
  
    while True:
        
        complete = " "
        
        if not ordered:
           order = input("Hello, would you like to order pizza or salad? ").lower().strip()
        else:
           order = input("Would you like to order pizza or salad? ").lower().strip()      
            
        if order == "done":
            if ordered:
                print("\nYour order is complete - Thank You! ")
                break
            else:
                print("\nNothing has been ordered at this time - Goodbye! ")
                break 
        
        elif order == "salad":
            print("\nYou have ordered a {0}.".format(salad()))
            ordered = True
            complete = input("Does that complete your order? (Yes or No) ").lower().strip()
        
        elif order == "pizza":
            print("\nYou have ordered a {0}.".format(pizza()))
            ordered = True
            complete = input("Does that complete your order? (Yes or No) ").lower().strip()
            
        else:
            print("\nPlease select one of the available options, or say 'done' to exit! ")

        while complete != "yes" and complete != "no" and complete != " ":
            print("\nPlease enter Yes or No! ")
            complete = input("Does that complete your order? (Yes or No) ").lower().strip()
        
        if complete == "yes":
            print("\nYour order is complete - Thank You! ")
            break
                 
def pizza():

    pizza_size = " "
    pizza_toppings = " "

    while True:

        pizza_size = input("Would you like a small, medium, or large? ").lower().strip()

        if pizza_size in ["small", "medium", "large"]:
            break
        else:
            print("\nPlease select one of the available options! ")

    pizza_toppings = toppings()
    
    if pizza_toppings:
        return "{0} pizza with {1}".format(pizza_size, " and ".join(pizza_toppings))
    else:
        return "{0} pizza".format(pizza_size)
    
def toppings():
    
    list_toppings = []
    
    while True:
        
        toppings = input("Would you like any toppings on your pizza? (Yes or No) ").lower().strip()
    
        if toppings == "yes":
            
            while True:
                
                choose_toppings = input("Would you like pepperoni, mushrooms, or spinach? (or say 'done' to exit) ").lower().strip()
                
                if choose_toppings in ["pepperoni", "mushrooms", "spinach"]:
                    list_toppings.append(choose_toppings)
                elif choose_toppings == "done":
                    return list_toppings
                else:
                    print("\nPlease select one of the available options, or say 'done' to exit! ")
        
        elif toppings == "no":
            break       
        else :
            print("\nPlease enter Yes or No! ")     
                
def salad():

  salad_type = " "
  salad_dressing = " "

  while True:
    
    salad_type = input("Would you like a Garden, Caesar, or Greek salad? ").lower().strip()

    if salad_type in ["garden", "caesar", "greek"]:
      break
    else:
      print("\nPlease select one of the available options! ")

  salad_dressing = dressing()
  
  if salad_dressing: 
      return "{0} salad with {1} dressing".format(salad_type, salad_dressing)
  else:
      return "{0} salad with no dressing".format(salad_type)

def dressing():
    
    while True:
        
        plain = input("Would you like any dressing on your salad? (Yes or No) ").lower().strip()
    
        if plain == "yes":
            
            while True:
                
                dressing = input("Would you like vinaigrette, ranch, blue cheese, or lemon dressing? ").lower().strip()
                
                if dressing in ["vinaigrette", "ranch", "blue cheese", "lemon"]:
                    return dressing
                else:
                    print("\nPlease select one of the available options! ")
        
        elif plain == "no":
            break      
        else :
            print("\nPlease enter Yes or No! ") 

if __name__ == '__main__':

   select_meal()
