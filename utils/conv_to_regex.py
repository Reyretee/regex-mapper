from utils.char_map import char_map
import re

def conv_to_regex(word):
    word = re.escape(word)
    regex_word = ''
    
    for char in word:
        if char in char_map:
            regex_word += char_map[char]
        else:
            regex_word += f'[{char}]'
    
    return fr'\b{regex_word}\b'