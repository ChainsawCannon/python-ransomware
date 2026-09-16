# Yet Another Python Ransomware
# LEGAL DISCLAIMER: THE FOLLOWING PROGRAM HAS BEEN CREATED FOR EDUCATIONAL PURPOSES ONLY. PLEASE DO NOT USE THIS REPOSITORY FOR CRIMINAL ACTIONS OR THIS REPOSITORY WILL BE TAKEN DOWN. IF RUNNING PLEASE RUN ON A VIRTUAL MACHINE!!

## About
  The following program is made to research how programs such as wannacry and other ransomware function. This program should at least encrypt files, I am currently working on a fix for decrypting files since that is currently non-functioning (despite encrypted file, invalidtoken error) ***IF RUNNING ON A VM AND YOU SOMEHOW HAVE IMPORTANT FILES ON IT PLEASE BACKUP ALL FILES BEFORE RUNNING SINCE THIS RANSOMWARE IS STILL WORK IN PROGRESS AND WILL DESTROY YOUR FILES.***

## How it works
  The main.py file will give options to encrypt or decrypt files, in this case encrypting files allows a user to select a directory of their choice and it feeds it to the encryption function. A key is generated using the Fernet symmetric encryption algorithm that gets saved to a key file. The encryption function will then go through your file directory with os.scandir(), skipping desktop.ini specifically for encryption and decryption due to being an important windows file for specific folders. Then with the generated key file from the keygen function encrypts files in the directory. 
  The decryption function would work similarly with the function obtaining the generated key from the encrypted key file, then it should go through a directory of a users choice and decrypt all files ***(this is currently bugged, should be fixed in a future update)***.
## Dependencies
  This program uses the cryptography library in python, please install it before using.
  This program also needs to be run in an admin console in order to function, otherwise you will get "Permission Denied" errors.

## What I would like to add
  To this program once I fix the bugs with file decryption/encryption I would like to add a GUI "ransom note" using tkinter and for Windows systems add a desktop wallpaper changing function to leave a similar ransom message. (Similar to that of something like Wannacry shown below)
![Screenshot of the wallpaper used on wannacry ransomware](https://media.licdn.com/dms/image/v2/C5612AQG8pqrkoblkJg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1520158949029?e=2147483647&v=beta&t=nfv6WkIDJzlASoK0luv7GwDhEBCy5QxB92Fvbg5ENXs)

## Projects that inspired this and resources I used
[Ransomware-PoC by Jimmy-ly00](https://github.com/jimmy-ly00/Ransomware-PoC)
[Python-Ransomware by ncorbuk](https://github.com/ncorbuk/Python-Ransomware)
[Simple Ransomware Script in Python by Emmanuel Munyite](https://dev.to/munyite001/simple-ransomware-script-in-python-48id)

Thanks for reading! - Shay (They/Them)

