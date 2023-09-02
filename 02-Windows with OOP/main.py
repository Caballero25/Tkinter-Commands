from tkinter import Button, Frame, Tk
from Application import Application

root = Tk()
root.title("Frames Examples")
root.geometry("400x200")

fram1 = Frame(root, bg="lightblue")
fram1.pack(expand=True, fill='both')
fram1.config(cursor='pirate')

fram2 = Frame(root, bg="lightgreen")
fram2.pack(expand=True, fill='both')
fram2.config(cursor='heart')

fram3 = Frame(root, bg="pink")
fram3.pack(expand=False, fill='both')
fram3.config(cursor='')

Redbutton = Button(fram1, text='red', fg="orange")
Bluebutton = Button(fram1, text='blue', fg="orange")
Greenbutton = Button(fram1, text='green', fg="orange")

Redbutton.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=0.9)
Bluebutton.place(relx=0.35, rely=0.05, relwidth=0.25, relheight=0.9)
Greenbutton.place(relx=0.65, rely=0.05, relwidth=0.25, relheight=0.9)

Blackbutton = Button(fram2, text='BLACK', bg='silver',fg="RED")
Blackbutton.pack()

app = Application(master=root)

root.mainloop()