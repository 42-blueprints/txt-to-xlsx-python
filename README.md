# Extract Data from TXT to XLSX

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description
This Python project extracts data from a text file (`.txt`) and writes it to an Excel file (`.xlsx`). It's designed to be a simple, yet powerful tool for converting and organizing textual data into a more manageable and structured format.

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
| Name    | ID        | Age |
|---------|-----------|-----|
| jose    | 391299    | 19  |
| pedro   | 12353     | 20  |
| carlos  | 12959812  | 60  |
| donuwu  | 0492      | 90  |

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [openpyxl](https://openpyxl.readthedocs.io/) - A Python library to read/write Excel 2010 xlsx/xlsm files.
- Your Name - Project creator and maintainer.
```

Replace `yourusername` with your GitHub username and `Your Name` with your actual name. If you have a `LICENSE` file, make sure it is correctly referenced. Adjust the `Examples` section as needed based on your specific input/output format.# txt-to-xlsx-python
