# Class for a download handler process
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
    
    
    
    def create_progress_bar(self):
        pass
    
    def __init__(self, url, bar_master, yt_dlp_path, output_path):
        self.url = url
        self.bar_master = bar_master
        self.yt_dlp_path = yt_dlp_path
        self.output_path = output_path
        self.progress = ctk.IntVar(bar_master, value=0)
        self.create_progress_bar()
    def start(self):
        thread = threading.Thread(target=self.download)
        thread.start()
        self.thread = thread
        
    
    def line_to_progress(self, line):
        print(line)
    def download(self):
        output = sp.Popen([self.yt_dlp_path, self.url, "-P", self.output_path, "--newline", "-q", "--progress"], stdout=sp.PIPE)
        for line in output.stdout: 
            if self.line_to_progress(line.decode()) != None:
                self.progress.set(self.line_to_progress(line.decode()))
