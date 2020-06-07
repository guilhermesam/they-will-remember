# Verify if a string is a palindrome
def is_palindrome(string):
    if isinstance(string, str):
        string = string.upper()
        if string[::-1] == string:
            return True
        else: 
            return False
    else:
        raise ValueError('param must be a str')
        
def caesar_cipher(string, shifties):
    if shifties >= 0:
        string = string.replace(' ','')
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_alphabet_pt1 = alphabet[:shifties]
        new_alphabet_pt2 = alphabet[shifties:]
        full_new_alphabet = new_alphabet_pt2 + new_alphabet_pt1
        encrypted_word = ''

        for letter in string:
            index = alphabet.index(letter)
            encrypted_word += full_new_alphabet[index]

        return encrypted_word
    else:
        raise ValueError('shifties must be an integer >= 0')

def leds(number): 
    if number >= 0:
        numbers_and_leds = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
        number = str(number)
        total = 0
        for n in number:
            total += numbers_and_leds[int(n)]
        return total
    else:
        raise ValueError('param must be an integer >= 0')
        
def to_camel_case(original_word):
    if original_word == '':
        return ''
    else:
        word = original_word.title()
        seps = ['_', '-']
        for item in seps:
            word = word.replace(item, ' ')

        if original_word[0].islower():
            word = word.replace(word[0], word[0].lower())
        word = word.replace(' ','')
        return word
