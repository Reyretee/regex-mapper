# regex-mapper

`regex-mapper` is a Python utility that converts words into regex patterns based on character mappings for flexible text matching and validation.

## Features

- Converts words into regex patterns using a specified character map.
- Reads words from the `words.txt` file and generates a regex pattern for each word.
- Outputs the generated regex patterns into an easily readable `output.yml` file.
- Handles special characters appropriately and manages file access errors.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Reyretee/regex-mapper.git
   ```

2. Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. Add the words you want to convert to regex in the words.txt file. Write each word on a separate line.

2. Run the script:
  ```bash
  python main.py
  ```

3. The output will be saved to the output.yml file. You can find the list of generated regex patterns there.


## Example

If the words.txt file contains:
```bash
test
hello
example
```
The output.yml file will contain the following regex patterns:
```bash
regex_list:
  - \b[t3s]{1}[eéê]{1}[sş]{1}[t3]{1}\b
  - \b[h]{1}[eéê]{1}[l1]{1}[l1]{1}[o0öó]{1}\b
  - \b[eéê]{1}[x]{1}[aáâä@4]{1}[m]{1}[p]{1}[l1]{1}[eéê3]{1}\b
  ```

