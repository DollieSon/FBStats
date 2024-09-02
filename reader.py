import os
import json
PATH = "C:\\Users\\ray anthony\\Downloads\\FB Something\\FB Something\\your_facebook_activity\\messages\\inbox\\"
PERSON_NAME = "Ray Anthony Dollison"

BANNED_SUBSTR = [
    "voted for",
    "sent an attachment",
    "sent a link"
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
        sender_name = message['sender_name']
        if sender_name not in container.keys():
            container[sender_name] = {}
        if PathName not in container[sender_name].keys():
            container[sender_name][PathName] = {}
        time = message['timestamp_ms']
        content = message['content']
        container[sender_name][PathName][time] = content

# Example usage:
files = list_files(PATH)
people = {

}
"""
"Name" : {

}
"""
for  file in files:
    # print(file)
    if file.endswith(".json"):
        NameTemp = (file.split("\\")[-2])
        Suffix = NameTemp.split("_")[-1]
        # print("Suffix : ", Suffix)
        ChatName = NameTemp.removesuffix("_"+Suffix)
        print(ChatName)
        with open(file,'r') as jason:
            data = json.load(jason)
            #Count the people if 2 then 1v1 else GC
            # if len(data['participants']) == 2: # Normal Convo
            #     for name in data['participants']:
            #         if name != PERSON_NAME:
            #             ChatName = name
            #             break
            filtered = get_messages(data['messages'],people,ChatName)
            # insert to people


with open("Saved.json","w") as outfile:
    json.dump(people,outfile)
            # need to insert person
            # print(data['participants'])
            # for message in messages:
                # people.append()





# print(files)