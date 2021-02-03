"""
Bases for a few frequently used CarrieAIAssistant plugin module command wake functions
"""

def key_word(command_string, key_words, ordered=False):
    """
    A wake function that searches for key words
    A specific order and be specified (but there may be no repeated words if so)
    Returns chance of waking
    """
    key_words_found = 0
    ordered_index = 0
    for i in command_string.split(" "):
        search_words = [key_words,key_words[ordered_index:]][ordered]
        if i.lower() in map(lambda x: x.lower(),search_words):
            key_words_found += 1
            ordered_index = command_string.split(" ").index(i)
    return key_words_found/len(key_words)

def multi_key_word(command_string, key_words, ordered = False):
    """
    A wake function that searches for key words
    Multiple keywords can be in place of one position
    A specific order and be specified (but there may be no repeated words if so)
    Returns chance of waking
    """
    key_words_copy = key_words.copy()
    for i in command_string.split(" "):
        for j in key_words_copy:
            if_list_contin = isinstance(j, list) and i.lower() in map(lambda x: x.lower(),j)
            if_string_contin = isinstance(j, str) and j.lower() == i.lower()
            if if_list_contin or if_string_contin:
                if ordered:
                    key_words_copy = key_words_copy[key_words_copy.index(j):]
                key_words_copy.remove(j)
    return (len(key_words)-len(key_words_copy))/len(key_words)
