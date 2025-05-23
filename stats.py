def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(chars_dict):
    """
    Convert a dictionary of characters and their counts to a sorted list of dictionaries.

    Args:
        chars_dict (dict): Dictionary with characters as keys and counts as values

    Returns:
        list: List of dictionaries sorted by count in descending order
              Each dictionary has format {"char": character, "num": count}
    """
    sorted_list = []

    # Convert the dictionary to a list of dictionaries with the required format
    for char, count in chars_dict.items():
        sorted_list.append({"char": char, "num": count})

    # Sort the list in descending order based on the "num" value
    sorted_list.sort(key=lambda x: x["num"], reverse=True)

    return sorted_list