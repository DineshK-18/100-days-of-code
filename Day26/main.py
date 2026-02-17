import pandas as pd
nato_df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter:row.code for (index, row) in nato_df.iterrows()}
user_input = input("Enter the text:").upper()

code_words = [nato_alphabet[char] for char in user_input]

print(code_words)