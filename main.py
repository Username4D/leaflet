import customtkinter as ctk
import subprocess as sp
import threading


# Setup

yt_dlp_path = "C:/Program Files/yt-dlp.exe"
output_path = "%USERPROFILE%/Videos"

active_threads = [] # All active download threads

# Download function

def download(url = "yt"):
    print("Started download of " + url)
    output = sp.run([yt_dlp_path, url, "-P", output_path], capture_output=True, text=True)
    for line in output.stdout:
        print(line, end="")

def create_download_thread(url = "yt"):
    download_thread = threading.Thread(target=download, kwargs={"url": url})
    active_threads.append(download_thread)
    download_thread.start()
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
download_button = ctk.CTkButton(master=download_area, text="download", command=lambda: create_download_thread(url=current_url.get()))
download_button.pack()

download_area.pack()
window.mainloop()
