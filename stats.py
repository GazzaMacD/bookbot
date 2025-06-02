def get_num_words(text):
    """Takes in a string of text and counts the number of individual words in
    the string"""
    count = len(text.split())
    return count


def get_char_count(text):
    """Takes in a string of text and counts the frequency of each character
    returned as a dictionary with each individual character as key and the
    value being the number of occurances of the charater in the string"""
    count = {}
    for char in text:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
