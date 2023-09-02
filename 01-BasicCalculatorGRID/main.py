#Para empaquetar la app y que no funcione por consola, cambiar la extensión a .pyw
from tkinter import Tk,Label,Button,Entry

#General data 
#Relative position = relx, rely, relwidth, relheight
#Absolute position = x, y, width, height


vent = Tk()
vent.title("Interfaz de práctica")
vent.resizable(0,0) #True or False (X, Y)
vent.iconbitmap("favicon.ico")
vent.geometry("650x350") #Width and height of the window
vent.config(bg="#fff", cursor="question_arrow") #Visual configurations of program


#Funcs
def fSuma():
    n1=txtNum1.get() #Get data of the input box
    n2=txtNum2.get()
    r=float(n1)+float(n2)
    txtNum3.delete(0,'end') #Deleted older content of the input
    txtNum3.insert(0,r)  #Insert result into txt box
    
#Labels, txt & buttons
lblNum1 = Label(vent,text="Primer Número: ",bg="yellow")
txtNum1=Entry(vent,bg="pink")
lblNum2 = Label(vent,text="Segundo Número: ",bg="yellow")
txtNum2=Entry(vent,bg="pink")
btn1=Button(vent,text="Sumar", command=fSuma)
lblNum3 = Label(vent,text="Resultado: ",bg="yellow")
txtNum3 = Entry(vent, bg="cyan")

#Grid position
lblNum1.grid(row=0,column=0,padx=6, pady=6, sticky="w",ipady=6) #pad = margin type #ipad = padding type 
txtNum1.grid(row=0,column=1,padx=6, pady=6)
lblNum2.grid(row=1,column=0,padx=6, pady=6, sticky="w",ipady=6)
txtNum2.grid(row=1,column=1,padx=6, pady=6)
btn1.grid(row=1,column=2,padx=6, pady=6, ipady=4, ipadx=10)
lblNum3.grid(row=2,column=0,padx=6, pady=6, sticky="w",ipady=6)
txtNum3.grid(row=2,column=1,padx=6, pady=6)



vent.mainloop()





