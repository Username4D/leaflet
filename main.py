from pickle import FRAME
from typing import Text
import customtkinter as ctk
import subprocess as sp

yt_dlp_path = "C:/Program Files/yt-dlp.exe"
output_path = "%USERPROFILE%/Videos"
# Download function
def download(url = "yt"):
    sp.run([yt_dlp_path, url, "-P", output_path], capture_output=True)
    


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
download_button = ctk.CTkButton(master=download_area, text="download", command=lambda: download(url=current_url.get()))
download_button.pack()

download_area.pack()
window.mainloop()
