from cryptography.fernet import Fernet
import os
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
                continue
            with open(entry, 'rb') as f:
                data = f.read()
                decrypted_file = fernet.decrypt(data)
            with open(entry, 'wb' ) as f:
                 f.write(decrypted_file)