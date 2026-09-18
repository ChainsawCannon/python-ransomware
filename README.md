# Yet Another Python Ransomware
# LEGAL DISCLAIMER: THE FOLLOWING PROGRAM HAS BEEN CREATED FOR EDUCATIONAL PURPOSES ONLY. PLEASE DO NOT USE THIS REPOSITORY FOR CRIMINAL ACTIONS OR THIS REPOSITORY WILL BE TAKEN DOWN. IF RUNNING PLEASE RUN ON A VIRTUAL MACHINE!!
![picture of ransomware running on a virtual machine](https://chainsawcannon.neocities.org/images/ransomwaretest.png)
## About
  The following program is made to research how programs such as wannacry and other ransomware function. This program encrypts and decrypts files.

## How it works
  The main.py file will give options to encrypt or decrypt files, in this case encrypting files allows a user to select a directory of their choice and it feeds it to the encryption function. A key is generated using the Fernet symmetric encryption algorithm that gets saved to a key file. The encryption function will then go through your file directory with os.scandir(), skipping desktop.ini specifically for encryption and decryption due to being an important windows file for specific folders. Then with the generated key file from the keygen function encrypts files in the directory. 
  The decryption function would work similarly with the function obtaining the generated key from the encrypted key file, then it should go through a directory of a users choice and decrypt all files (it should work now).
## Dependencies
  This program uses the cryptography library in python, please install it before using.
  This program also needs to be run in an admin console in order to function, otherwise you will get "Permission Denied" errors.

## What I would like to add
  So far, the GUI has been added. I would like to add a text box that you can enter the key into and it automatically decrypts files without having to reopen the program. I would also still like to add wallpaper changing eventually.

## Projects that inspired this and resources I used
[Ransomware-PoC by Jimmy-ly00](https://github.com/jimmy-ly00/Ransomware-PoC),
[Python-Ransomware by ncorbuk](https://github.com/ncorbuk/Python-Ransomware),
[Simple Ransomware Script in Python by Emmanuel Munyite](https://dev.to/munyite001/simple-ransomware-script-in-python-48id)

Thanks for reading! - Shay (They/Them)

