# Name: Ariana Fafach
# Date: 2/13/2026
# Title: Program #5: Bank Balance


# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 0.0         #initialize for while loop

    ######################

    # Get budgeted amount from user:
    budget = float(input("Enter the amount that you have budgeted for the month:  "))
    
    # Set the value of 'expense' equal to anything other than zero to run the loop:
    expense = 1

    while expense != 0:
        # Get the expense vaulues from the user:
        expense = float(input("Enter another expense or 0 to quit:  "))
        
        # Accumulate the expenses:
        spent += expense

    # Calculate the difference between budgeted and spent:
    difference = budget - spent 

    # Display messages for all different values of 'difference':
    if difference > 0:
        print(f"You are under budget by ${difference:,.2f}!")
    
    elif difference == 0:
        print(f"You are right on your budgeted amount.")
    
    elif difference < 0:
        print(f"You are over budget by ${abs(difference):,.2f}.")

    ######################


if __name__ == '__main__':
    main()