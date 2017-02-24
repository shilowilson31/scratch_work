
#Calculate Meal and tip based on use input.
def calculator(tip) : 
    meal = float(input("How much did the meal cost? ")) 
    tax=.07*meal
    subtotal = meal + tax 
    tip=subtotal*(tip/100)
    total=subtotal+tip
    print ("Meal: $%.2f \nTax: $%.2f \nSubtotal: $%.2f\nTip: $%.2f\nTotal: $%.2f" 
           % (meal, tax,subtotal,tip,total))
    return
tip = float(input("How much percent would you like to tip?"))
calculator(tip)