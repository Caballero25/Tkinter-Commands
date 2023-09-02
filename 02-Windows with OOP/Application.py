import tkinter as tk 

class Application(tk.Frame):
    def __init__(self, master=None): #Constructor of the main root - required
        super().__init__(master) 
        self.master = master 
        self['bg']="orange"
        self.pack(expand=True, fill='both')
        self.create_widgets()
    
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n Click me!"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self)
        self.quit["text"] = "Close application"
        self.quit["command"] = self.master.destroy  #Destroy function closes the root
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hello users")
