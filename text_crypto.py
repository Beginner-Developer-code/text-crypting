import tkinter as tk
from tkinter import ttk
import cryptography
from cryptography.fernet import Fernet
from datetime import datetime
import os

def crypto():
    text = entry_text.get()
    home_directory = os.path.expanduser("~")

    if text != "":
        key = Fernet.generate_key()
        token = Fernet(key)
        text_encrypt = token.encrypt(text.encode("utf-8"))

        with open(f"{home_directory}/Scrivania/secret_file.txt", "a") as file:
            file.write(f"\n\n{datetime.now()}\n")
            file.write(f"Secret Key: {key.decode("utf-8")}\n")
            file.write(f"Text encrypt: {text_encrypt.decode("utf-8")}")

        result_encrypt.configure(text="File creato correttamente!")
        screen.after(3000, lambda: result_encrypt.configure(text="In attesa..."))
    else:
        result_encrypt.configure(text="Inserisci un testo!")

def decrypt():
    key = entry_key.get()
    text = entry2_text.get()

    if key != "" and text != "":
        try:
            token = Fernet(key.encode("utf-8"))
            text_decrypt = token.decrypt(text.encode("utf-8"))
            result_decrypt.configure(text=f"Text decrypt: {text_decrypt.decode("utf-8")}")
        except (ValueError,cryptography.fernet.InvalidToken):
            result_decrypt.configure(text="Uno o entrambi i campi contengono valori errati!")
    else:
        result_decrypt.configure(text="Riempi entrambi i campi!")


screen = tk.Tk()
screen.title("TextCrypting")
screen.geometry("800x800")
screen.resizable(False, False)
screen.configure(background="darkgrey")

#widgets

app_title = ttk.Label(screen, text="TextCrypting", font=("Helvetica", 30, "bold"), background="darkgrey").pack(pady=20)

#Frame1
frame_encrypt = tk.Frame(screen, bg="lightgrey", width=600, height=300)
frame_encrypt.pack_propagate(False)
frame_encrypt.pack(pady=20)

frame1_title = ttk.Label(frame_encrypt, text="Encrypt", font=("Helvetica",18,"bold"), background="lightgrey").pack(pady=10)
text_label = ttk.Label(frame_encrypt, text="TEXT", background="lightgrey", font=("Courier New",12)).pack(pady=12)
entry_text = ttk.Entry(frame_encrypt, width=50, justify="center", font=("Courier New",12))
entry_text.pack()
encrypt_button = ttk.Button(frame_encrypt, text="Encrypt Text", cursor="hand2", command=crypto).pack(pady=25)
result_encrypt = ttk.Label(frame_encrypt, text="In attesa...",background="lightgrey" ,font=("Helvetica",15,"bold"))
result_encrypt.pack(pady=10)

#Frame2
frame_decrypt = tk.Frame(screen, bg="lightgrey", width=600, height=300)
frame_decrypt.pack_propagate(False)
frame_decrypt.pack(pady=20)

frame2_title = ttk.Label(frame_decrypt, text="Decrypt", font=("Helvetica",18,"bold"), background="lightgrey").pack(pady=10)
text2_label = ttk.Label(frame_decrypt, text="TEXT", background="lightgrey", font=("Courier New",12)).pack(pady=12)
entry2_text = ttk.Entry(frame_decrypt, width=50, justify="center", font=("Courier New",12))
entry2_text.pack()
text2_label = ttk.Label(frame_decrypt, text="KEY", background="lightgrey", font=("Courier New",12)).pack(pady=12)
entry_key = ttk.Entry(frame_decrypt, width=50, justify="center", font=("Courier New",12))
entry_key.pack()
decrypt_button = ttk.Button(frame_decrypt, text="Decrypt Text", cursor="hand2", command=decrypt).pack(pady=20)
result_decrypt = ttk.Label(frame_decrypt, text="In attesa...", background="lightgrey" ,font=("Helvetica",15,"bold"))
result_decrypt.pack(pady=5)


screen.mainloop()