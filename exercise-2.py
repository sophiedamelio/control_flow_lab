# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.


# submission = input('enter a word or phrase ')
# print(len(submission)

phrase = ''

while phrase != 'quit': 
    phrase = input('Please enter a word or phrase: ').lower()
    length_of_phrase = len(phrase)

    print(f'What you entered is {length_of_phrase} characters long')

