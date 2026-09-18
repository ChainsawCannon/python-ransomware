from cryptography.fernet import Fernet
import os
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
                        continue
                    with open(entry, 'rb') as f:
                        data = f.read()
                        encrypted_file = fernet.encrypt(data)
                    with open(entry, 'wb') as ef:
                        ef.write(encrypted_file)
            print("Encryption complete.")
        case 'n':
            print("Encryption Cancelled.")

