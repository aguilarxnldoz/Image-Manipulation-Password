from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''



def k_load():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = k_load()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:", user, "| Password: ", 
                fer.decrypt(passw.encode()).decode())
                

def add():
    name = input('Enter account name: ')
    pwd = input("Enter a password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to [VIEW] or [ADD] passwords or [QUIT]- ").upper()
    if mode == "QUIT":
        break
    if mode == "VIEW":
        view()
    elif mode == "ADD":
        add()
    else:
        print("Invalid Option...")