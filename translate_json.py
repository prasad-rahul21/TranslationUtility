import pandas as pd
import argparse
import json

def load_translation_map(excel_path):
    df = pd.read_excel(excel_path)
    if 'Label' not in df.columns or 'Translation' not in df.columns:
        raise ValueError("Excel must have 'Label' and 'Translation' columns.")
    return dict(zip(df['Label'], df['Translation']))

def process_json_file(input_path, output_path, translation_map):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    translated_data = {}
    for key, value in data.items():
        translated_value = translation_map.get(value, value)
        translated_data[key] = translated_value

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Translation complete. Output saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Translate values in JSON using an Excel translation file.")
    parser.add_argument('--input', required=True, help="Path to input JSON file.")
    parser.add_argument('--excel', required=True, help="Path to Excel file with translations.")
    parser.add_argument('--output', default='output.json', help="Path to save the translated output.")
    args = parser.parse_args()

    translation_map = load_translation_map(args.excel)
    process_json_file(args.input, args.output, translation_map)

if __name__ == "__main__":
    main()
