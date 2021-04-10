#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.path = tk.StringVar()
        self.question = tk.StringVar()
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.path_label = tk.Label(self)
        self.path_label["text"] = "Path to School questions: "
        self.path_label.grid(row=1,column=1,sticky="E")

        self.path_text = tk.Entry(self,width=80)
        self.path_text.grid(row=1,column=2,padx=10)
        self.path_text["textvariable"] = self.path

        self.path_button = tk.Button(self)
        self.path_button["text"] = ". . ."
        self.path_button["command"] = self.get_path
        self.path_button.grid(row=1,column=3)

        self.question_label = tk.Label(self)
        self.question_label["text"] = "Question: "
        self.question_label.grid(row=2,column=1,sticky="E")

        self.question_text = tk.Entry(self,width=80)
        self.question_text.grid(row=2,column=2,padx=10)
        self.question_text["textvariable"] = self.question

        self.process_button = tk.Button(self, text="Process", fg="red", command=self.process)
        self.process_button.grid(row=3,column=2,padx=10,pady=5,sticky="E")

        self.edit_button = tk.Button(self, text="Open&Edit Temporary Textfile", command=self.open_textfile)
        self.edit_button.grid(row=4,column=2,padx=10,pady=5)

        self.edit_button = tk.Button(self, text="Open Folder", command=self.open_folder)
        self.edit_button.grid(row=5,column=2,padx=10,pady=5)

        self.edit_button = tk.Button(self, text="Generate Chart", fg="red", command=self.generate_chart)
        self.edit_button.grid(row=6,column=2,padx=10,pady=5)

    def get_path(self):
        self.path.set(tk.filedialog.askopenfilename(initialdir = os.path.dirname(os.path.realpath(__file__)), title = "Select a File", filetypes = (("CSV files","*.csv*"),("all files","*.*"))))

    def process(self):
        # ... call the external function here
        pass

    def generate_chart(self):
        #call external function
        pass
    
    def open_textfile(self):
        os.system("notepad {}".format(self.path.get()))
    
    def open_folder(self):
        os.system("explorer {}".format(os.path.dirname(self.path.get())).replace("/","\\"))


root = tk.Tk()
root.title("Symphony Questions")
root.geometry("720x200")
app = Application(master=root)
app.mainloop()