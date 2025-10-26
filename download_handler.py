# Class for a download handler process
from sys import stderr
import threading
import subprocess as sp
import pathlib
import customtkinter as ctk

class download_handler_object:
    url = ""
    bar_master = None
    thread = None
    yt_dlp_path = pathlib.Path("")
    output_path = pathlib.Path("")
    progressbar = None
    window = None
    output = None
    def create_progress_bar(self):
        self.progress = ctk.DoubleVar(value=0)
        self.progressbar = ctk.CTkProgressBar(master=self.bar_master, variable=self.progress)
        self.progressbar.grid(row=3, column=1, pady=10)
    
    def __init__(self, url, bar_master, yt_dlp_path, output_path, window):
        self.url = url
        self.bar_master = bar_master
        self.yt_dlp_path = yt_dlp_path
        self.output_path = output_path
        self.progress = ctk.IntVar(bar_master, value=0)
        self.window = window
        self.create_progress_bar()
    def start(self):
        thread = threading.Thread(target=self.download)
        thread.start()
        self.thread = thread
    
        
    
    def line_to_progress(self, line):
        try:
            return float(line[10:].split("%")[0] ) / 100
        except:
            pass
    def download(self):
        self.output = sp.Popen([self.yt_dlp_path, self.url, "-P", self.output_path, "--newline", "-q", "--progress"], stdout=sp.PIPE, stderr=sp.PIPE)
        for line in self.output.stdout:
            
            if self.line_to_progress(line.decode()) != None:
                self.progress.set(self.line_to_progress(line.decode()))
            
        for line in self.output.stderr:
            if line[:6] == b'ERROR:':
                self.window.show_error(line)
            
        self.progressbar.grid_forget()
    def kill(self):
        self.output.kill()
        print("process killed")
        self.thread = None
