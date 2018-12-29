# This practice problem was to create a GUI that would an input of Kg, then convert it to grams, punds, and ounces.

from tkinter import *

window = Tk()

# Function to convert from kg to grams, pounds, and ounces
def kg_to_others():
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.20462
    ounces = float(e1_value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", ounces)
    t3.insert(END, ounces)

# Kg label
lab = Label(window,text="Kg")
lab.grid(row=0,column=0)

# Button to execute the function
b1= Button(window, text="Convert",command=kg_to_others)
b1.grid(row=0, column=2)

# Entry widget for the Kg value
e1_value = StringVar()
e1= Entry(window, textvariable= e1_value)
e1.grid(row=0, column=1)

# 3 Text widgets for the converted values to appear 
t1= Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2= Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3= Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()