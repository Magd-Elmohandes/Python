from tkinter import *

def x():
    gram= round(float(st1.get())*1000,2)
    pound= round(float(st1.get())*2.20462,2)
    ounce= round(float(st1.get())*35.274,2)
    t1.delete(0.0,END)
    t1.insert(END,str(gram)+" gram")
    t2.delete(0.0,END)
    t2.insert(END,str(pound)+" pound")
    t3.delete(0.0,END)
    t3.insert(END,str(ounce)+" ounce")

Magd=Tk()

st1=StringVar()
lab1=Label(Magd,text = "kg")
lab1.grid(row=0)
e1= Entry(Magd, textvariable=st1)
e1.grid(row=0,column=1)
b1=Button(Magd,text="Convert",command=x)
b1.grid(row=0,column=2)
t1= Text(Magd,height=1,width=30)
t1.grid(row=1)
t2= Text(Magd,height=1,width=30)
t2.grid(row=1,column=1)
t3= Text(Magd,height=1,width=30)
t3.grid(row=1,column=2)

Magd.mainloop()
