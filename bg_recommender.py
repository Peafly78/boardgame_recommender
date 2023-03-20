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


# TESTING

#selection = autocomplete("hell", ["hello", "hell", "help", "ginger", "love", "held"]) # returns a list
#print(selection)

#choices = number_options(selection) # returns a dictionary
#print(choices)

#show = display_numbered_options(choices) # returns a list
#print(show)