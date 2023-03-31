# Import games data

from games_data import boardgame_collection, boardgame_types
from linkedlist import Node, LinkedList

# Insert data into LinkedList datastructure

bg_types = LinkedList()
for type in boardgame_types:
    bg_types.insert_beginning(type)

bg_collection = LinkedList()
for game in boardgame_collection:
    bg_collection.insert_beginning(game)

# Testing data structure

#print(bg_types.stringify_list())
#print()
#print(bg_collection.stringify_list())


# Autocomplete functionality

def autocomplete(string, options):
    """Checks if the words in a list start with the string given and returns a new list with matching words.
    Required Arguments: string, list of words
    Example: autocomplete("hel", ["hello", "ginger", "help"]) will return ["hello", "help"]
    """
    selection = list()
    for option in options:
        if option.startswith(string):
            selection.append(option)
    return selection


def number_options(options):
    numbered_options = dict()
    for num in range(1, len(options)+1):
        numbered_options[num] = options[num-1]
    return numbered_options


def display_numbered_options(numbered_options):
    display = list()
    for key, val in numbered_options.items():
        display_value = val + " -> (" + str(key) + ")"
        display.append(display_value)
    return display


# Testing Autocomplete

#selection = autocomplete("hell", ["hello", "hell", "help", "ginger", "love", "held"]) # returns a list
#print(selection)

#choices = number_options(selection) # returns a dictionary
#print(choices)

#show = display_numbered_options(choices) # returns a list
#print(show)



# Further function definitions

def check_for_criteria(value_list, user_input):
    return (user_input[0] >= value_list[2] and user_input[0] <= value_list[3]) and (value_list[4] > user_input[2]*0.7 and value_list[4] < user_input[2]*1.3) and (user_input[1] >= value_list[5])

def filter_linked_list(ll, user_input):
    bg_results = list()
    current_node = ll.head_node
    while current_node:
        if current_node.get_value() != None:
            if check_for_criteria(current_node.get_value(), user_input):
                bg_results.append(current_node.get_value())
        current_node = current_node.get_next_node()
    return bg_results

def get_numeric_user_input(question, min, max):
    user_input = input(question)
    while not isinstance(user_input, int):
        try:
            user_input = int(user_input)
        except:
            user_input = input(f"Please, enter a valid number between {min} and {max}.")
        else:
            if user_input in range(min, max+1):
                return user_input
            user_input = input(f"Please, enter a valid number between {min} and {max}.")
    return user_input

def collecting_all_user_input():
    print("\nWelcome to the boardgame recommender!\n\n\nI need some data to give you a playing recommendation:")
    input_collection = list()

    num_players_param = ("\nHow many people will be playing?\n> ", 1, 9)
    num_players = get_numeric_user_input(*num_players_param)
    input_collection.append(num_players)

    youngest_player_param = ("\nHow old is the youngest player?\n> ", 1, 99)
    youngest_player = get_numeric_user_input(*youngest_player_param)
    input_collection.append(youngest_player)

    playing_time_param = ("\nHow long should the game approximately take to play?\nPlease enter the time in minutes.\n> ", 5, 240)
    playing_time = get_numeric_user_input(*playing_time_param)
    input_collection.append(playing_time)

    game_type = input("\nWhat type of boardgame would you like to play? Enter the first character(s) and hit enter to have some options displayed.\n> ")
    auto_complete_options = autocomplete(game_type, boardgame_types)
    while not auto_complete_options:
        game_type = input("Sorry, no options available for the characters you entered.\nPlease try again.\n> ")
        auto_complete_options = autocomplete(game_type, boardgame_types)
    numbered_options = number_options(auto_complete_options)
    options_display = display_numbered_options(numbered_options)
    print(options_display) 

    selected_type = None
    choice = input("Please, type the number next to the boardgame type you would like to play.\n> ")
    while not isinstance(choice, int):
        try:
            choice = int(choice)
        except ValueError:
            choice = input("\nPlease enter a valid number, displayed next to the desired boardgame type.\n> ")
        else:
            try:
                selected_type = numbered_options[choice]
            except KeyError:
                choice = input("\nThis is not a valid option. Please, try again.\n> ")
    input_collection.append(selected_type)
    return input_collection

def display_results(all_inputs):
    print(f"\nSo, you would like to play a {all_inputs[3]} game that takes approximately {all_inputs[2]} minutes.\nThere are {all_inputs[0]} people playing and the youngest player is {all_inputs[1]} years old.")
    print("\nHere are your results:\n")
    print(22 * "*")
    result = filter_linked_list(bg_collection, all_inputs)
    if not result:
        print("\nSorry, no games found that fit your criteria.")
    else:
        print("\nYou can play:")
        for game in result:
            print("*", game[0])

def start_over():
    choice = input("\nAre you happy with your results? (y)\nIf not you can start over. (n)\n> ")
    while choice.lower() not in ("y", "n"):
        choice = input("\nPlease enter 'y' for yes or 'n' for no, meaning the selection process starts over.")
    while choice.lower() != "y":
        new_inputs = collecting_all_user_input()
        display_results(new_inputs)
        start_over()
    print("\nThanks for using the Boardgame Recommender!\n\n*** HAVE FUN PLAYING! ***")
    return
        

# Function calls

all_inputs = collecting_all_user_input()
display_results(all_inputs)
start_over()