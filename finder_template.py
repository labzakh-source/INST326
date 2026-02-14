import sys
import argparse
"""
Driver: Lina Abzakh
Navigator:Jayant Ranabhat
Assignment """

HOME_DATABASE = {
"name":["shoes", "papers", "picture frames", "tshirts", "soccer balls", "kitchen tables", "cabinets"],
"location":["floor", "cubbard", "wall", "cubbard", "basket", "floor", "corner"],
"date last moved": ["8/23/23", "7/23/23", "6/23/23", "1/13/23", "2/9/22", "3/23/23", "5/30/23"],
"time last moved": ["10:00am", "1:00am", "10:00pm", "9:00am", "12:00pm", "4:00pm", "10:30pm"]
}

def main(NEW_DATABASE)
    name = input("What item are you looking for?: ")
    NEW_DATABASE = {}
    output = f"The {name} were found in the {location} and were placed there on {date last moved} at {time
    last moved}"
    return output
    


    

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
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
    parser.add_argument('object', type=str, help="Please enter the name that we are searching for.")
    
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

    print(main(arguments.object))