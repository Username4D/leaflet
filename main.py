from pickle import FRAME
from typing import Text
import customtkinter as ctk

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
download_button = ctk.CTkButton(master=download_area, text="download", command=lambda: print(current_url.get()))
download_button.pack()

download_area.pack()
window.mainloop()
