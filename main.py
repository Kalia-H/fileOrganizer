import os
path_to_directory = "C:/programs/filesourceproject/sortfiles"
if os.path.isdir(path_to_directory):
    all_items = os.listdir(path_to_directory)
    #print(f"files in {path_to_directory} : {all_items} ")  --testing 
    files = []
    directory = []
    for item in all_items:
        item_path = os.path.join(path_to_directory, item)
        if os.path.isfile(item_path):
            files.append(item)
        elif os.path.isdir(item_path):
            directory.append(item)
        else:
            print(f"Unknown item type: {item}")
    #print(f"Files: {files} \n Directories: {directory}")   --testing 
    categorized_files = {
        "JSON": [],
        "HTML": [],
        "TEXT": [],
        "CSV": []
    }
    json_extensions = ['.json']
    html_extensions = ['.html']
    text_extensions = ['.txt']
    csv_extensions = ['.csv']
    for category in categorized_files.keys():
        subdirectory_path = os.path.join(path_to_directory, category)
        if not os.path.exists(subdirectory_path):
            os.makedirs(subdirectory_path)
            print(f"Subdirectory created: {subdirectory_path}")
        else:
            print(f"Subdirectory: {subdirectory_path} already exists.")
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        #print(f"split file[i]: {file_extension}")  --testing 
        if file_extension in json_extensions:
            categorized_files["JSON"].append(file)
        elif file_extension in html_extensions:
            categorized_files["HTML"].append(file)
        elif file_extension in text_extensions:
            categorized_files["TEXT"].append(file)
        elif file_extension in csv_extensions:
            categorized_files["CSV"].append(file)
        
    #print('JSON files: ', categorized_files["JSON"])   --testing 
    #print('HTML files: ', categorized_files["HTML"])   --testing 
    #print('TEXT files: ', categorized_files["TEXT"])   --testing 
    #print('CSV files: ', categorized_files["CSV"])     --testing 
else :
    print(f"the directory {path_to_directory} does not exist")