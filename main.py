import re
import yaml
import os


char_map = {
    'a': '[aáâä@4]',
    'b': '[b8]',
    'c': '[cç]',
    'd': '[d]',
    'e': '[eéê3]',
    'f': '[f]',
    'g': '[gğ9]',
    'h': '[h]',
    'i': '[i1!İ]',
    'j': '[j]',
    'k': '[kq]',
    'l': '[l1]',
    'm': '[m]',
    'n': '[n]',
    'o': '[o0öó]',
    'p': '[p]',
    'r': '[r]',
    's': '[sş5$]',
    't': '[t]',
    'u': '[uüûú]',
    'v': '[v]',
    'y': '[y]',
    'z': '[z2]'
}

def conv_to_regex(word):
    word = re.escape(word)
    regex_word = ''
    
    for char in word:
        regex_word  += char_map.get(char.lower(), f'[{char}]')
    return fr'\b{regex_word}\b'

input_file = 'words.txt'
output_file = 'output.yml'

if not os.path.isfile(input_file):
    print(f'File {input_file} not found')
else:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    regex_list = []
    for word in lines:
        word = word.strip()
        if word:
            regex_list.append(conv_to_regex(word))

    with open(output_file, 'w', encoding='utf-8') as yaml_file:
        yaml.dump(
            {
                'regex_list': regex_list
            },
            yaml_file,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False
        )
    print("output.yml dosyası oluşturuldu.")