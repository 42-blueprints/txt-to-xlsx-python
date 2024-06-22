# !!! THIS IS A EXPERIMENTAL PROJECT...

# Extract Data from TXT to XLSX

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Project Description
This Python project extracts data from a text file (`.txt`) and writes it to an Excel file (`.xlsx`). It's designed to be simple.

## Features
- Extracts data from a structured text file.
- Writes data to an Excel file with multiple sheets.
- Handles various data formats and structures.
- Provides a simple command-line interface.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/txt-to-xlsx.git
   cd txt-to-xlsx
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Place your `.txt` file in the project directory.

2. Run the script:
   ```sh
   python extract_data.py input.txt output.xlsx
   ```

   Replace `input.txt` with the path to your text file and `output.xlsx` with the desired name of the Excel file.

## Examples
### Input (`input.txt`)
```
jose
391299
19

pedro
12353
20

carlos
12959812
60

donuwu
0492
90
```

### Command
```sh
python extract_data.py input.txt output.xlsx
```

### Output (`output.xlsx`)
| Name    | Number    | Age |
|---------|-----------|-----|
| jose    | 391299    | 19  |
| pedro   | 12353     | 20  |
| carlos  | 12959812  | 60  |
| donuwu  | 0492      | 90  |


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

