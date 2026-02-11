# Name: Ariana Fafach
# Date: 2/11/2026
# Title: Program #2: Movie Tix


# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():

    ######################
    
    # get the name of the first movie
    movie = input("Enter the name of the movie or quit to quit: ")

    # set the initial value for total_tickets equal to zero
    total_tickets = 0

    # while loop to get the total number of tickets
    while movie != 'quit':

        # get the number of tickets for the movie
        tickets = int(input("Enter the number of tickets you want for that movie: "))

        # get the name of the next movie
        movie = input("Enter the name of the movie or quit to quit: ")

        # add the number of tickets for the current movie to the total number of tickets
        total_tickets += tickets
    
    # Display the total number of tickets
    print(f"You need a total of {total_tickets:,} tickets.")
    
    ######################



if __name__ == '__main__':
    main()