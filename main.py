import os
path_to_directory = "C:/programs/filesourceproject/sortfiles"
if os.path.isdir(path_to_directory):
    files = os.listdir(path_to_directory)
    print(f"files in {path_to_directory} : {files} ")
else :
    print(f"the directory {path_to_directory} does not exist")