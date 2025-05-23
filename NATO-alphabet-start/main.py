import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
def game():
    nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
    print(nato_dict)
    user_input = input("Enter a word: \n").upper()
    list_word = [letter for letter in user_input]
    try:
        result = [nato_dict[letter] for letter in list_word]

    except KeyError:
        print("Sorry, that word is not in the alphabet.")
        game()
    else:
        print(result)
game()
