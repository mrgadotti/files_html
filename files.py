import os
import json

def create_file_list_json(folder_path):
    file_list = []
    
    # Get all files in the folder
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_info = {
                "name": file_name,
                "desc": file_name.split('.')[0].capitalize()  # Extracting file name without extension
            }
            file_list.append(file_info)
    
    # Create a dictionary with the file list
    data = {"files": file_list}
    
    # Convert the dictionary to JSON format
    json_data = json.dumps(data, indent=4)
    
    # Write the JSON data to a file
    with open("files.json", "w") as json_file:
        json_file.write(json_data)

# Provide the path to the folder
folder_path = "."

# Call the function to create the JSON file
create_file_list_json(folder_path)

