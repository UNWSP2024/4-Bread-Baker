# Name: Ariana Fafach
# Date: 2/12/2026
# Title: Program #3: Average Rainfall


# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.


    ######################

# Get the number of years from user:
years = int(input("Enter the number of years you want to calculate the average rainfall of:  "))

# Set the total inches of rainfall to zero:
total_rain = 0

# First for loop runs once for every year.
for i in range(1, years + 1):
    
    # Set the year's rain to zero:
    years_rain = 0
    
    # Second for loop runs once for every month.
    for x in range(1,13):
        
        # Get inches of rainfall for every month:
        rain = int(input(f"Enter the number of inches of rain that fell in month {x} of year {i}:  "))
        
        # Add each month's rain fall to the total rainfall for that year:
        years_rain += rain

    # Add each year's rainfall to the total rainfall of all the years:
    total_rain += years_rain

# Calculate total number of months:
total_months = years*12

# Calculate average rainfall per month:
average_rain = total_rain/total_months

# Display total number of months:
print(f"The total number of months is {total_months:,}.")

# Display the total rainfall:
print(f"The total rainfall for the entire period is {total_rain:,} inches.")

# Display the average rainfall per month:
print(f"The average rain per month is {average_rain:,.2f} inches.")

    ######################    

