import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
import ssl
import os
from PIL import Image, ImageTk

ssl._create_default_https_context = ssl._create_unverified_context

# Funzione per scaricare il video
def download_video():
    video_url = entry.get()

    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        desktop_path = os.path.expanduser("~/Desktop")
        download_path = os.path.join(desktop_path, yt.title)
        stream.download(output_path=download_path)
        status_label.config(text="Download completato! Il video è stato salvato sul desktop.")
    except Exception as e:
        status_label.config(text=f"Errore: {str(e)}")

# Creazione della finestra principale
window = tk.Tk()
window.title("YouTube Video Downloader")

# Funzione per mostrare informazioni "Learn More"
def show_about():
    about_message = "YouTube Downloader v1.0\nAuthor: gabricampaa\n\nFollow me on:\nInstagram: https://www.instagram.com/gabricampaa/\nGitHub: https://github.com/gabricampaa\n\nI did this cause i was tired of ads thrown at me every second on websites... and cause i enjoy programming! See ya!"
    
    messagebox.showinfo("Learn More", about_message)

# Creazione di una barra dei menu
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Creazione di un menu "About"
info_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=info_menu)

# Aggiungi un elemento "Learn More..." con una funzione di gestione
info_menu.add_command(label="Learn More...", command=show_about)

# Creazione dell'etichetta e dell'area di inserimento del link
link_label = tk.Label(window, text="Insert YT link:")
link_label.pack()
entry = tk.Entry(window, width=40)
entry.pack()

# download button
download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()




#Centering the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 400
window_height = 150
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Executing main window
window.mainloop()
