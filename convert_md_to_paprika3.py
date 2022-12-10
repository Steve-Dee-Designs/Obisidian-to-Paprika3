import os
import re

def convert_md_to_paprika3(file_path):
    # read the contents of the file
    with open(file_path, "r") as f:
        contents = f.read()
    # perform formatting operations on the text
    formatted_contents = re.sub(r"# (.*)", r"<h1>\1</h1>", contents)
    formatted_contents = re.sub(r"## (.*)", r"<h2>\1</h2>", formatted_contents)
    formatted_contents = re.sub(r"### (.*)", r"<h3>\1</h3>", formatted_contents)
    formatted_contents = re.sub(r"\*\*(.*)\*\*", r"<strong>\1</strong>", formatted_contents)
    formatted_contents = re.sub(r"_(.*)_", r"<em>\1</em>", formatted_contents)
    # write the formatted text to a new file
    with open(file_path[:-3] + ".paprika3", "w") as f:
        f.write(formatted_contents)

# get a list of all the files in the folder
folder_path = "/path/to/folder"
files = os.listdir(folder_path)
# convert each file to Paprika3 format
for file in files:
    # only convert files with the .md extension
    if file.endswith(".md"):
        file_path = os.path.join(folder_path, file)
        convert_md_to_paprika3(file_path)