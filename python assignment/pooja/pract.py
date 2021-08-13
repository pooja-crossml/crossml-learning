#!/usr/bin/python3

from datetime import datetime
import getpass
import os.path
import json
import random

# Access system time
time = datetime.now().time().strftime('%H:%M:%S')
print(f"Time: {time}")

# access user data
username = getpass.getuser()
print("Username: "+ username)

# will access the home directory
parent_dir = os.path.expanduser("~print(")
files_loc = parent_dir+'/users/'

folder_path = os.getcwd()+'/users/'
# print(folder_path)
all_files = os.listdir(os.getcwd()+'/users/')
print()



class DataInfo:
    users_name=[]
    def read_data(self, folderpath, allfiles):
        self.folderpath = folderpath
        self.allfiles = allfiles
        users_name=[]
        for files in allfiles:
            # print(files)
            file_data = open(self.folderpath+files, "r")
            for names in file_data:
                users_name.append(names.strip())

            file_data.close()
        return users_name


    def generate_uuid(self, users):
        self.users = users
        # print(users)
        for user in users:
            b=random.randint(1000,9000000000)
            # print(user.split())
            name = user.split()

        return hex(b)+name[0]

# Generate email for every user
    def generate_email(self, user):
        self.user = user
        print(user)
        first_name = user.split()[0]
        last_name = user.split()[1]
        # print(first_name +' '+last_name)

        email = first_name +"_"+ last_name[0]+ "@virtual.com"
        return email

# convert data into json
    def data_convert_into_json(self,users):
        self.users = users
        user_data = []
        for user_name in users:
            user_data.append({self.generate_uuid(user_name):{"username":user_name,"email":self.generate_email(user_name)}})

        return json.dumps(user_data)

mydata = DataInfo()
users_list = mydata.read_data(folder_path,all_files)
output= mydata.data_convert_into_json(users_list)
json_output = open("json_output.json","w")
json_output.writelines(str(output))
json_output.close()
