import customtkinter as ctk
import ui.icons as icons

class home_screen():
    url_bar = None
    current_url = None
    download_button = None
    error_label = None
    def __init__(self, window):
        window.grid_rowconfigure(1, weight=4)
        window.grid_rowconfigure(2, weight=1)
        window.grid_rowconfigure(3, weight=1)
        window.grid_rowconfigure(4, weight=1)
        window.grid_rowconfigure(5, weight=1)
        window.grid_rowconfigure(6, weight=4)
        window.grid_columnconfigure(1, weight=1)
        
        # Title:
        font = ctk.CTkFont(family="Calibri", size=50, weight="bold")
        title = ctk.CTkLabel(master=window, text="DOWNLOAD ANYTHING", anchor="center", font=font)
        title.grid(padx=80 ,column=1, row=2, sticky="ews")
        
        # URL Bar:
        self.current_url = ctk.StringVar(master=window, value="")
        self.url_bar = ctk.CTkEntry(master=window, placeholder_text="Enter any URL...", textvariable=self.current_url, fg_color="#090909")
        self.url_bar.grid(padx = 80, column=1, row=3, sticky="ew")
        
        # Download Button:
        def download_pressed():
            window.create_download_thread(url=self.current_url.get(), master=window)
            self.url_bar.grid_forget()
            try:
                self.error_label.grid_forget()
            except:
                pass
        self.download_button = ctk.CTkButton(master=window, text="   Download", command=lambda: download_pressed(), image=icons.download, compound="right", anchor="center")
        print(self.current_url.get())
        self.download_button.grid(column=1, row=4, sticky = "n", padx = 240)
        
        
        # Error:
        error_font = ctk.CTkFont(family="Calibri")
        self.error_label = ctk.CTkLabel(text="", font=error_font, master=window)
    def show_error(self, error=""):
        self.url_bar.grid(padx = 80, column=1, row=3, sticky="ew")
        self.error_label.configure(text=error)
        self.error_label.grid(row=5, column= 1, sticky="n")
    
    def show_success(self):
        self.url_bar.grid(padx = 80, column=1, row=3, sticky="ew")
