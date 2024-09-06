import json

def convert_txt_to_json(txt_file, json_file):
    # Open the .txt file and read lines
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Strip newlines and create a list of options
    options = [line.strip() for line in lines if line.strip()]  # Remove empty lines
    
    # Write the list to a .json file
    with open(json_file, 'w', encoding='utf-8') as json_out:
        json.dump(options, json_out, ensure_ascii=False, indent=4)
    
    print(f"Successfully converted {txt_file} to {json_file}")

# Example usage:
convert_txt_to_json('bad_options.txt', 'bad_options.json')
convert_txt_to_json('good_options.txt', 'good_options.json')
