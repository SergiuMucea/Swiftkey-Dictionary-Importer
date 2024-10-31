import json
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo, showerror
from tqdm import tqdm

def find_word(lines) -> str:
    for line in lines[1:]:
        if line.strip():  # Check if line is not empty
            gboard_word = line.strip().split()[0]
            break
    return gboard_word

def find_line(lines, gboard_word) -> int:
    for idx, line in enumerate(lines):
        if gboard_word in line:
            return idx + 1


def process_swiftkey(swift_word) -> None:
    with open(gboard_dictionary, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    gboard_word = find_word(lines)
    line_idx = find_line(lines, gboard_word)

    # Insert new line and duplicate gboard_word line
    lines.insert(line_idx, lines[line_idx - 1])
    lines[line_idx] = lines[line_idx - 1]
    
    # Process Swiftkey word by changing gboard_word with swift_word
    lines[line_idx] = lines[line_idx].replace(gboard_word, swift_word)

    with open(gboard_dictionary, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def integrate_swift_dict() -> None:
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        swift_words = data.get("terms", [])
    
    print("Integrating Microsoft SwiftKey...\n")
    for word in tqdm(swift_words):
        if word.isalpha() and len(word) > 3:  # processing only words with more than 3 characters
            process_swiftkey(word)

gboard_dictionary = askopenfilename(title="Select your Gboard Dictionary")
json_file = askopenfilename(title="Select your SwiftKey dictionary")

# Handling all Exception messages in one statement, just to have some sort of a message if something goes wrong.
try:
    integrate_swift_dict()
except Exception as e:
    showerror(title="Error", message=f"Something went wrong. Make sure you selected the correct file(s).\n{e}")
else:
    showinfo(title="Info", message="Microsoft SwiftKey dictionary integrated successfully")