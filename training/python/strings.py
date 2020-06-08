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
        raise ValueError('shifties must be an integer >= 0'
 
# Transform a string from snake_case to camelCase
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
    
# Returns an list of tuples, which contains each unique letter in the 
# original_word and the number of times each one appears
def ordered_count(original_word):
    unique_elements = []
    for char in original_word:
        if char not in unique_elements:
            unique_elements.append(char)
    count_elements = [original_word.count(x) for x in unique_elements]
    return list(zip(unique_elements, count_elements))

# Build the figure of a diamond with *, receiving the max length of the figure as param                         
def diamond(times):
    if times <= 0 or times % 2 == 0:
        return None
    stars = [x for x in range(1, times+1, 2)] 
    stars += list(reversed(stars[:-1]))
    spaces_range = [x for x in range(stars.index(max(stars)), -1, -1)]
    spaces_range += list(reversed(spaces_range[:-1]))
    diam = ''
    for item in range(0, len(stars)):
        diam += spaces_range[item]* " " + stars[item] * '*' + '\n'
    return diam
