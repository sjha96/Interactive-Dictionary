import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        user_input = input("Did you mean " + close_match + " instead? Enter Y if yes, or N if no: ")
        if user_input.lower() == "y":
            return data[close_match]
        elif user_input.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "Please only type in Y or N"
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
