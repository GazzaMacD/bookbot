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


def sorted_char_count(char_count):
    """Takes in a dictionary of chars as keys along with number of chars as values. Returns
    a from max to min sorted list of dictionaries with the character and the count"""
    sorted_char_counts = []
    for k, v in char_count.items():
        sorted_char_counts.append({"char": k, "num": v})

    sorted_char_counts.sort(reverse=True, key=lambda d: d["num"])
    return sorted_char_counts
