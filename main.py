import customtkinter as ctk
import subprocess as sp
import threading
import download_handler
import pathlib

# Setup

yt_dlp_path = pathlib.Path("C:/Program Files/yt-dlp.exe")
output_path = pathlib.Path("%USERPROFILE%/Videos")

download_handlers = []

def create_download_thread(url = "yt", master = None):
    handler = download_handler.download_handler_object(url, master, yt_dlp_path, output_path)
    download_handlers.append(handler)
    handler.start()
# Window
window = ctk.CTk()
window.geometry("200x200")

# Download area
download_area = ctk.CTkFrame(master=window)

# Url bar
current_url = ctk.StringVar(value="")
url_bar_label = ctk.CTkLabel(master=download_area, text="URL:")
url_bar_label.pack()
url_bar = ctk.CTkEntry(master=download_area, textvariable=current_url)
url_bar.pack()

# Download button
download_button = ctk.CTkButton(master=download_area, text="download", command=lambda: create_download_thread(url=current_url.get(), master=window))
download_button.pack()

download_area.pack()
window.mainloop()
