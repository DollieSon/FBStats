import os
import json
PATH = "C:\\Users\\ray anthony\\Downloads\\FB Something\\FB Something\\your_facebook_activity\\messages\\inbox\\"


def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# test = "Hello_World"

# Example usage:
files = list_files(PATH)
people = []
for  file in files:
    # print(file)
    if file.endswith(".json"):
        NameTemp = (file.split("\\")[-2])
        Suffix = NameTemp.split("_")[-1]
        # print("Suffix : ", Suffix)
        Name = NameTemp.removesuffix("_"+Suffix)
        print(Name)
        with open(file,'r') as jason:
            data = json.load(jason)
            messages = data['messages']
            # print(data['participants'])
            # for message in messages:
                # people.append()



"""
[
    "Chat_Name":[
        [
            "Timestamp" : "Content"
        ]
    ]
]
"""

# print(files)