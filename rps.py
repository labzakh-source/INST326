"""
Driver: Lina Abzakh
Navigator: Jessica Persaud
Assignment: INST326 Rock, Paper, Scissors
Date: 2_6_26

Challenges Encountered: Navigating interaction with terminal, it was a first for the both of us and we struggled
a bit when trying to impliment the users chosen names, I realized we forgot to add and f in front of the 
returned statement, like so f"{p1} blahh". Other than that the logic was done in one sitting without error
"""

import sys
import argparse
import os

def determine_winner(p1, p2):
    #if else statements determining winner for every possible outcome
    if p1 == 'r' and p2 == 'p':
        return 'player2'
    elif p1 == 's' and p2 == 'p':
        return 'player1'
    elif p1 == 'p' and p2 =='s':
        return 'player2'
    elif p1 == 'p' and p2 == 'r':
        return 'player1'
    elif p1 == 'r' and p2 == 's':
        return 'player1'
    elif p1 == 's' and p2 == 'r':
        return 'player2'
    elif p1 == 'r' and p2 == 'r':
        return 'tie'
    elif p1 == 'p' and p2 == 'p':
        return 'tie'
    elif p1 == 's' and p2 == 's':
        return 'tie'

        
    

def main(player1_name, player2_name):
    #prompts users for name and action
    p1 = input(f"Enter {player1_name}'s hand shape ('r', 'p', or 's'): ")
    p2 = input(f"Enter {player2_name}'s hand shape ('r', 'p', or 's'): ")
    #as well as print statements for every possible outcome
    
    if determine_winner(p1, p2) == 'player2':
        print(f"{player2_name} wins!")
    elif determine_winner(p1, p2) == 'player1':
        print(f"{player1_name} wins!")
    elif determine_winner(p1, p2) == 'tie':
        print("Tie!")

    

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments
    Args:
    args_list (list) : the list of strings from the command prompt
    Returns:
    args (ArgumentParser)
    """
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations commence.
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    
    parser.add_argument('p1_name', type=str, help="Please enter Player1's Name")
    parser.add_argument('p2_name', type=str, help="Please enter Player2's Name")
    
    args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.
    
    return args

if __name__ == "__main__":
    
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?

    #It the script is being run as a module, the block of code under this will not beexecuted.
    #If the script is being run natively, the block of code below this will be executed.

    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.

    main(arguments.p1_name, arguments.p2_name)