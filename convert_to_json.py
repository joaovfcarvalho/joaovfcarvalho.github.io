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
convert_txt_to_json('C:/Users/joaov/OneDrive/Documents/jogo_do_ou_app/bad_options.txt', 'C:/Users/joaov/OneDrive/Documents/jogo_do_ou_app/bad_options.json')
convert_txt_to_json('C:/Users/joaov/OneDrive/Documents/jogo_do_ou_app/good_options.txt', 'C:/Users/joaov/OneDrive/Documents/jogo_do_ou_app/good_options.json')
