import json
import os
import base64
import hashlib
from cryptography.fernet import Fernet

data_file= "password.json"
master_file= "master.key"

#________________master password________________
def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def master_password():
    password=input("set master password: ")
    key =  generate_key(password)
    with open(master_file,"wb") as f:
        f.write(key)
         
    print("master password set succesfully.")
    
def verify_master_password():
    if not os.path.exists(master_file):
        print("Master password not found!.setting up.......")
        master_password()
        
    password = input("enter master password: ")
    key = generate_key(password)
    with open(master_file,"rb") as f:
        saved_key = f.read(key) 
       
    if key==saved_key:
        return key
    else:
        print("wrong password!")
        return None
    
#________________data handling___________________
def load_data():
    if not os.path.exists(data_file):
        return {}
    
    with open(data_file,"r") as f:
        return json.load(f)
    
def saved_data(data):
    with open(data_file,"w") as f:
        json.dump(data,f,indent=4)

#_______________password operation_______________
def add_password(fernet):
    site=input("website: ")
    username=input("Username: ")
    password=input("Password: ")
    
    encrypted = fernet.encrypt(password.encode()).decode()
    data = load_data()
    data[site]={"username":username,"password":encrypted}
    
    saved_data(data)
    print("password saved..")
    
def lists_sites():
    data=load_data()
    if not data:
        print("no saved data")
        return
    for site in data:
        print(f"- {site}")
        
def retrieve_password(fernet):
    site=input("website: ")
    data=load_data()
    
    if site not in data:
        print("no data found.")
        return
    
    encrypted= data[site]["password"]
    decrypted=fernet.decrypt(encrypted.encode()).decode()
    print(f"username: {data[site]['username']}")
    print(f"password: {decrypted}")
    
#____________main menu______________
def main():
    key=verify_master_password()
    if not key:
        return
    fernet=Fernet(key)
    
    while True:
        print("\n-----password manager-----")
        print("1-Add password: ")
        print("2-View password: ")
        print("3-Get password: ")
        print("4-Exit")
        
        choice=input("choice: ")
        if choice=="1":
            add_password(fernet)
        elif choice=="2":
            lists_sites()
        elif choice=="3":
            retrieve_password(fernet)
        elif choice=="4":
            break
        else:
            print("invalid choice!")

if __name__=="__main__":
    main()