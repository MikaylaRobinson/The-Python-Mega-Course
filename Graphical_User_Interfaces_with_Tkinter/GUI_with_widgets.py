from tkinter import *

# Creating the actual window
window = Tk()

def km_to_miles():
    miles= float(e1_value.get())*1.6
    t1.insert(END,miles)

# Creating the button and adding it to the window
b1= Button(window, text="Execute",command=km_to_miles)
b1.grid(row=0, column=0)

# Adding an entry widget
e1_value= StringVar()
e1= Entry(window, textvariable= e1_value)
e1.grid(row=0, column=1)

# Adding a text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)
 
window.mainloop()
