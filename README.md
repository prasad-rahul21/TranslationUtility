# Translation Utility

## Overview
This utility translates values in a JSON file using a mapping provided in an Excel file. It is designed to handle large JSON files and gracefully manage cases where translations are missing.

## Features
- Translates values in a JSON file based on an Excel mapping.
- Handles cases where translations are missing by assigning "TRANSLATION WAS NOT FOUND".
- Ignores unused labels in the Excel file.
- Supports large JSON files.

## Prerequisites
- Python 3.x
- Required Python libraries:
  - `pandas`
  - `openpyxl`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd TranslationUtility
   ```
2. Install the required Python libraries:
   ```bash
   pip install pandas openpyxl
   ```

## Usage
Run the script using the command line:
```bash
python translate_json.py --input <input.json> --excel <translationFile.xlsx> --output <output.json>
```

### Arguments
- `--input`: Path to the input JSON file (required).
- `--excel`: Path to the Excel file containing translations (required).
- `--output`: Path to save the translated JSON file (optional, defaults to `output.json`).

### Example
#### Input JSON (`input.json`):
```json
{
    "key1": "value1",
    "key2": "value2"
}
```

#### Excel File (`translationFile.xlsx`):
| Label   | Translation |
|---------|-------------|
| value1  | translated1 |
| value3  | translated3 |

#### Command:
```bash
python translate_json.py --input input.json --excel translationFile.xlsx --output output.json
```

#### Output JSON (`output.json`):
```json
{
    "key1": "translated1",
    "key2": "TRANSLATION WAS NOT FOUND"
}
```

## Notes
- Ensure the Excel file has two columns: `Label` and `Translation`.
- If a value in the JSON file is not found in the Excel file, the script assigns "TRANSLATION WAS NOT FOUND" as the translated value.
- Unused labels in the Excel file are ignored.
- Name of the excel and input json should be matched or else the command should be modified accordingly.