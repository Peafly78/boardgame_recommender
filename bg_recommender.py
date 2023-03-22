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


# Data

boardgame_types = ["family", "dexterity", "party", "abstract", "strategic", "thematic", "euro", "war", "dice", "cards", "deck building", "bluffing", "cooperative", "children", "fighting", "area control", "legacy", "drafting", "memory", "miniatures", "engine building", "educational", "roleplaying"]

boardgame_collection = {
    "dict_explanation" : [["tags/categories/types"], "minimum number of players", "maximum number of players", "average playing time in minutes", "minimum player age"],
    "Braendi Dog" : [["family", "cooperative"], 3, 6, 60, 8],
    "Ligretto" : [["cards", "abstract", "dexterity"], 2, 4, 20, 8],
    "Ciao Giuseppe" : [["cards", "abstract"], 2, 6, 20, 6],
    "Monopoly" : [["engine building", "strategic"], 2, 6, 120, 10],
    "Spinderella" : [["family", "thematic"], 2, 4, 20, 6],
    "Ligretto Dice" : [["dice", "abstract", "dexterity"], 2, 6, 10, 8]
}


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

choice = input("Please, type the number next to the boardgame type you would like to play.\n> ")
while choice not in numbered_options.keys():
    while not isinstance(choice, int):
        try:
            choice = int(choice)
        except:
            choice = input("\nPlease enter a valid number, displayed next to the desired boardgame type.\n> ")
input_collection.append(choice)

# selected_type = numbered_options[choice]
# input_collection.append(selected_type)


# Testing

print(input_collection)


