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

def filter_boardgame_collection(user_input):
    boardgame_results = dict()
    for key, value in boardgame_collection.items():
        if user_input[0] >= int(boardgame_collection[key][1]) and user_input[0] <= int(boardgame_collection[key][2]):
            boardgame_results[key] = value
    copy_of_results = dict(boardgame_results)
    for key, value in copy_of_results.items():
        if value[3] < user_input[2]*0.75 or value[3] > user_input[2]*1.25:
            del boardgame_results[key]
    copy_of_results = dict(boardgame_results)
    for key, value in copy_of_results.items():
        if not user_input[1] >= int(value[4]):
            del boardgame_results[key]
    return list(boardgame_results)


            

# User Input

print("Welcome to the boardgame recommender!")
input_collection = list()

num_players = input("\nI need some data to give you a playing recommendation:\nHow many people will be playing?\n> ")
while len(num_players) != 1:
    num_players = input("\nPlease, enter a number between 1 and 9.\n> ")
while not isinstance(num_players, int):
    if num_players in "123456789":
        num_players = int(num_players)
    else:
        num_players = input("\nPlease, enter a valid number between 1 and 9.\n> ")
input_collection.append(num_players)

youngest = input("\nHow old is the youngest player?\n> ")
while not isinstance(youngest, int):
    try:
        youngest = int(youngest)
    except:
        youngest = input("\nPlease enter a valid number between 1 and 99.\n> ")
input_collection.append(youngest)

playing_time = input("\nHow long should the game approximately take to play?\nPlease enter the time in minutes.\n> ")
while not isinstance(playing_time, int):
    try:
        playing_time = int(playing_time)
    except:
        playing_time = input("\nPlease enter a valid number, e.g. 30 for half an hour of playing time.\n> ")
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

print(f"So, you would like to play a {selected_type} game that takes approximately {playing_time} minutes.\nThere are {num_players} people playing and the youngest player is {youngest} years old.")
print()
print("Here are your results:")
print()
print(22 * "*")
print()
result = filter_boardgame_collection(input_collection)
if not result:
    print("Sorry, couldn't find a game matching your input.")
else:
    print("You can play:")
    for game in result:
        print("*", game)


# Testing




