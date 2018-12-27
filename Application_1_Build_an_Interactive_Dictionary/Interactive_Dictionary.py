# This short program allows a user to input a word and receive the definition. 

import simplejson as json
import difflib

# Load the json file as a python dictionary
# This file includes words as keys and their definitions as values
def_data = json.load(open("data.json"))

# Set up an input to make the dictionary search interactive
word = input("Please enter a word to find its definition: ")


def define_words(word):
    # The lower method is used to correct inconsistent capitalization
    word = word.lower()
    if word in def_data:
        return def_data.get(word)
    # Using title allows for proper nouns to be found in the dictionary
    elif word.title() in def_data:
        return def_data.get(word.title())
    # Upper allows for acronyms such as USA to be found
    elif word.upper() in def_data:
        return def_data.get(word.upper())
    # If the word is misspelled, the program will provide the closest possible match
    elif len(difflib.get_close_matches(word, def_data.keys(), 1)) >0:
        suggestion = difflib.get_close_matches(word, def_data.keys(), 1)
        clarification = input("Did you mean %s? [Y/N] Enter Y if yes, or N if no: " %suggestion[0]) 
        # The user must select if the suggested match is their intended outcome
        if clarification == "Y":
            return def_data.get(suggestion[0])
        elif clarification == "N":
            return "Please double check your word and try again."
        else:
            return "Not a valid response, please check your word and try again."
    else:
        return "Word not found. Please double check it and try again."
     
response = define_words(word)

# The definitions automatically appear as lists. Removing the list format makes the response more readable. 
if type(response) == list:
    for content in response:
        print(content)
else:
    print(response)