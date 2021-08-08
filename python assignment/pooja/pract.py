#!/usr/bin/python3

from datetime import datetime
import getpass
import os.path
import json
time = datetime.now().time().strftime('%H:%M:%S')
print(f"Time: {time}")
# This will access the current user

username = getpass.getuser()
print("Username: "+ username)
print()

# will access the home directory
parent_dir = os.path.expanduser("~")
files_loc = parent_dir+'/users/'
# print(parent_dir)
print(files_loc)

# import pathlib
# it will check the current working directory's path
# print(pathlib.Path.cwd()) #error while concating value.

folder_path = os.getcwd()+'/users/'
# print(folder_path)
all_files = os.listdir(os.getcwd()+'/users/')
print(all_files)
# creating a list of files.

users_name=[]
for files in all_files:
    file_data = open(folder_path+files, "r")
    for names in file_data:
        users_name.append(names.strip())
    file_data.close()

# print(users_name)
import random
def uniq_uuid(users):
    # n = random.randint(1,9000000000)
    # print(hex(n))
    # b=hex(n)
    for user in users:
        b=random.randint(1000,9000000000)
        # print(user.split())
        name = user.split()
        # print(user)
        # print(hex(b)+name[0])
    return hex(b)+name[0]

# print(uniq_uuid(users_name))
uniq_uuid(users_name)

def generate_email(users):
    for user in users:
        first_name = user.split()[0]
        last_name = user.split()[1]
        email = first_name +"_"+ last_name[0]+ "@virtual.com"
    return email

print(generate_email(users_name))
user_data =[]
for user_name in users_name:
    user_data.append({uniq_uuid(users_name):{"username":user_name,"email":generate_email(users_name)}})

print(json.dumps(user_data))

json_output = open("json_output.txt","w")
json_output.writelines(str(user_data))
json_output.close()