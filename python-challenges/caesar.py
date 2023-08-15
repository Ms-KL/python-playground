# https://realpython.com/python-practice-problems/
    # cd python-challenges
    # python caesar.py

'''
Caesar Cipher: 
    * a simple substitution cipher in which: 
        * each letter of the plain text is substituted with:
            * a letter found by: 
                * moving n places down the alphabet. 

eg: assume the input plain text is the following:
abcd xyz

If the shift value (n) = 4:
    then the encrypted text would be the following:
        efgh bcd
        a -> 4 places -> e
        b -> f
        c -> g
        d -> h
        x -> b
        y -> c
        z -> d

TASK:
You are to write a function that: 
* accepts two arguments: 
    1) a plain-text message
    2) number of letters to shift in the cipher. 
    
* The function will return:
    * an encrypted string with: 
        1) all letters transformed
        2) all punctuation and whitespace remaining unchanged

Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.

'''

def caesar(text_message, shift):

    '''
    this function: 
        * takes a text message and shift as input 
        * converts text letters to lowercase
        * finds position of letters in text message
        * checks for and preserves values for spaces and punctuation
        * adds shift value to position of letter value
            * checks if new position will exceed limit (123)
            * removes 26 from position if new position exceeds 123 limit
        * finds character of new position
        * returns a transformed text message using new positions

    ord = provides position number of character
    chr = provides character of position number
    
    '''
    
    result_as_string = ""

    for letter in text_message:
        letter = letter.lower()

        # find position for letter in text_message
        position = ord(letter)

        # add shift to position of letter if higher than 96 (lowercase letter index) - preserves characters and spacing
        if position > 96:
            position += shift

        # position is higher than 123 (after lower index), minus 26 to reset the flow of letters/numbers
        if position > 123:
            position -= 26

        # find letter from position
        new_letter = str(chr(position))

        # add to result
        result_as_string += new_letter

    return result_as_string

print(caesar("ABCD xYZ!", 4))

# RealPython solution alt (not providing parameters for special characters or upper)

# import string

# def caesar(text_message, shift):

#     # convert letters to lowercase and access positions with ascii
#     letters = string.ascii_lowercase
#     print(letters)

#     # slice letters from the "shift" starting position
#     # slice the remaining letters
#     # add them together
#     shifted_letters = letters[shift:] + letters[:shift]
#     print(shifted_letters)

#     # return value as a string
#     result_as_string = str.maketrans(letters, shifted_letters)

#     return text_message.translate(result_as_string)

# print(caesar("abcd xyz", 4))
