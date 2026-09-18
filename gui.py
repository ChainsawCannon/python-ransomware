import tkinter as tk
import ctypes
import os
def gui():
    ransom = tk.Tk()

    ransom.geometry("800x500")
    ransom.title("YOUR FILES HAVE BEEN ENCRYPTED")

    label = tk.Label(ransom, text="Your files have been encrypted by the encryptinator ransomware!!", font=(20))
    label2 = tk.Label(ransom, text="you have 24 hours to send monero to this address: thisisnotarealransomwarejustrunthefileagainandselectdecrypt", font=20)
    label.pack()
    label2.pack()
    ransom.mainloop()