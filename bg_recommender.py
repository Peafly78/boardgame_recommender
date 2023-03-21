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


# Testing

print(num_players, type(num_players))


