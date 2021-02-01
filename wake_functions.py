"""
Bases for a few frequently used CarrieAIAssistant plugin module command wake functions
"""

def key_word(command_string, key_words, ordered=False):
    """
    A wake function that searches for key words, a specific order and be specified.
    Returns chance of waking
    """
    key_words_found = 0
    ordered_index = 0
    for i in command_string.split(" "):
        unordered_check = not(ordered) and i.lower() in map(lambda x: x.lower(),key_words)
        ordered_check = ordered and i.lower() in map(lambda x: x.lower(),key_words[ordered_index:])
        if unordered_check or ordered_check:
            key_words_found += 1
            ordered_index = i
    return key_words_found/len(key_words)
