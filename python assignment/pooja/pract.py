'''
    This project will convert the file data into json data and stores its output
    in a file in dixtonary format.

'''
#!/usr/bin/python3
'''
    importing all the required libraries
'''
from datetime import datetime
import getpass
import os.path
import json
import random

'''
    Access system time
'''
time = datetime.now().time().strftime('%H:%M:%S')
print(f"Time: {time}")

'''
    access user data
'''
username = getpass.getuser()
print("Username: "+ username)

'''
    will access the home directory
'''
parent_dir = os.path.expanduser("~print(")
files_loc = parent_dir+'/users/'


'''
    creating a complete path
'''
folder_path = os.getcwd()+'/users/'
all_files = os.listdir(os.getcwd()+'/users/')
print()

class DataInfo:
    '''
        this class will read data from files, generate uuid, email user name and then create a json file
    '''
    users_name=[]
    def read_data(self, folderpath, allfiles):
        '''
            this method will read aal the names from the given file
        '''
        self.folderpath = folderpath
        self.allfiles = allfiles
        users_name=[]
        for files in allfiles:
            file_data = open(self.folderpath+files, "r")
            for names in file_data:
                users_name.append(names.strip())
            file_data.close()
        return users_name

    def generate_uuid(self, users):
        '''
            This method will generate uuid
        '''
        self.users = users
        for user in users:
            b=random.randint(1000,9000000000)
            name = user.split()
        return hex(b)+name[0]

    def generate_email(self, user):
        '''
            This method will generate email for every user
        '''
        self.user = user
        print(user)
        first_name = user.split()[0]
        last_name = user.split()[1]
        email = first_name +"_"+ last_name[0]+ "@virtual.com"
        return email

    def data_convert_into_json(self,users):
        '''
            This method will convert data into json
        '''
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
