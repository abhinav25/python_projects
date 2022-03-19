# importing module
import json
import os
import glob

# open json file and read data
with open("C:/Users/a42/OneDrive - UHG/Py/config_wordsearch.json", 'r') as json_file:
    config_data = json.load(json_file)
# print(config_data)
words = config_data.get('NON_USER_ID')
# print(words)
folder_path = config_data.get('FOLDER_PATH')
# print(folder_path)
No_of_files = len(os.listdir(folder_path))
print('File Count:', No_of_files)
keyword_found = []
for i in words:
    print('Keyword to be searched:', [i])
    keyword = i
    for filename in glob.glob(os.path.join(folder_path, '*.xml')):
        with open(os.path.join(os.getcwd(), filename), 'r', encoding='utf-8') as f:   # open in readonly mode
            text = f.read()
            print(filename)
            # print(text)
            if keyword in text:
                keyword_found.append([keyword, filename])
print('Result:', keyword_found)



