# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


# make list of vowels
# if input letter matches IN
# letter = input('Enter a letter a-z ')
# if letter in ('a', 'e', 'i', 'o', 'u'):
# 	print("%s is a vowel." % letter)
# else:
# 	print("%s is a consonant." % letter)

letter = ''

letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
print(f'The user entered {letter}')

if letter == 'a':
    print(f'{letter} is a vowel')
elif letter == 'e':
    print(f'{letter} is a vowel')
elif letter == 'i':
    print(f'{letter} is a vowel')
elif letter == 'o':
    print(f'{letter} is a vowel')
elif letter == 'u':
    print(f'{letter} is a vowel')
else:
    print(f'{letter} is a consonant')
