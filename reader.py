import os
import json
import random
import re
PATH = "C:\\Users\\ray anthony\\Downloads\\FB Something\\FB Something\\your_facebook_activity\\messages\\inbox\\"
PERSON_NAME = "Ray Anthony Dollison"
BANNED_REGEX = [
    r"((.* )?[rR]eacted .+ to your message)",
    r"this poll is no longer available",
    r".* left the group",
    r".* pinned a message",
    r".* sent an attachment",
    r".* send a live location",
    r".* added .* to the group",
    r".* set .* nickname to .*"
]




def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list
"""
    {
        "Name":{
            "Timestamp":"Content"
        }
    }
"""
def get_messages(messages,container,PathName):

    for message in messages :
        if 'content' not in message.keys():
            continue
        for regex in BANNED_REGEX:
            if re.match(regex,message['content']):
                print(message['content'])
                continue
        sender_name = message['sender_name']
        if sender_name not in container.keys():
            container[sender_name] = {}
        if PathName not in container[sender_name].keys():
            container[sender_name][PathName] = {}
        time = message['timestamp_ms']
        content = message['content']
        container[sender_name][PathName][time] = content

#Parsing FIles
files = list_files(PATH)
people = {

}
"""
"Name" : {

}
"""
print("found :" +str(len(files))+" files")
for  file in files:
    # print(file)
    if file.endswith(".json"):
        NameTemp = (file.split("\\")[-2])
        Suffix = NameTemp.split("_")[-1]
        # print("Suffix : ", Suffix)
        ChatName = NameTemp.removesuffix("_"+Suffix)
        # print(ChatName)
        with open(file,'r') as jason:
            data = json.load(jason)
            filtered = get_messages(data['messages'],people,ChatName)


BANNED_CHAR =  ["\\","/","*","?","<",">",":","|"]
def safe_name(name) -> str:
    for char in BANNED_CHAR:
        if char in name:
            return name.split(char)[0] + str(random.randint(0,100))
    return name

#File Saving 
print("saving...")
for filename in people.keys():
    # print(filename)
    with open("./Saved_Names/"+safe_name(filename)+".json","w") as outfile:
        json.dump(people[filename],outfile)
            # need to insert person
            # print(data['participants'])
            # for message in messages:
                # people.append()





# print(files)