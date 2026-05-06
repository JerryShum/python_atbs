# Write a function named is_pangram(sentence) that accepts a string argument, then returns True if it’s a pangram and False if not. A pangram is a sentence that uses all 26 letters of the alphabet at least once. For example, “The quick brown fox jumps over the yellow lazy dog” is a pangram.

# There are several ways to accomplish this task. One way is to have a variable named EACH_LETTER that starts as an empty list. Then, you can loop over the characters in the string argument, convert each to uppercase with the upper() method, and append it to the EACH_LETTER list if it is a letter and doesn’t already exist there. You can tell that a letter in char isn’t already in the EACH_LETTER list because the expression char not in EACH_LETTER will evaluate to True. After looping over each character in the user’s string, you’ll know that the string is a pangram if len(EACH_LETTER) evaluates to 26.

def is_pangram(sentence):
    # pangram --> 26 letters of the alphabet
    
    each_letter = []
    for char in sentence:
        if char.isalpha() and char.upper() not in each_letter:
            each_letter.append(char.upper())
        print(each_letter)
    
    if len(each_letter) == 26:
        return True
    
    return False
        
        
def main():
    userInput = input('Enter sentence > ')
    valid = is_pangram(userInput)
    
    
    if valid:
        print('This is a valid pangram.')

    else:
        print('This is NOT a valid pangram.')

main()