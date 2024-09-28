import os
import yaml
from utils.conv_to_regex import conv_to_regex

input_file = 'words.txt'
output_file = 'output.yml'

try:
    if not os.path.isfile(input_file):
        print(f'File {input_file} not found')
    else:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        regex_list = tuple(conv_to_regex(word.strip()) for word in lines if word.strip())
        
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
        print("Output file created successfully.")
except FileNotFoundError:
    print(f'File {input_file} not found')
except IOError as e:
    print(f'Error reading input file: {e}')
except yaml.YAMLError as e:
    print(f'Error creating YAML file: {e}')
except Exception as e:
    print(f'An unknown error occurred: {e}')