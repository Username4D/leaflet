import customtkinter as ctk
import download_handler
import pathlib
import ui.home_window
import ui.window_background
# Setup

yt_dlp_path = pathlib.Path("C:/Program Files/yt-dlp.exe")
output_path = pathlib.Path("%USERPROFILE%/Videos")

download_handlers = []


# App

class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        self.configure(fg_color = "#090909")
        
    def create_download_thread(self, url, master):
        handler = download_handler.download_handler_object(url, master, yt_dlp_path, output_path, self)
        download_handlers.append(handler)
        handler.start()
    def show_error(self, error=""):
        home_window.show_error(error=error)
    def show_success(self):
        home_window.show_success()
        
app = app()

# Main window
home_window = ui.home_window.home_screen(window=app)



app.mainloop()
