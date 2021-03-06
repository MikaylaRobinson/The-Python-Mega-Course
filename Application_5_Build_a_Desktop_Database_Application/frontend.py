'''
This is a program that will store certain info about books.
It will include:
Title
Author,
Year,
ISBN

The interface will allow the user to:
View all records
Search for an entry
Add an entry
Update an entry
Delete an entry
Close the program
'''
from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tupule
        index = listbox.curselection()[0]
        selected_tupule = listbox.get(index)

        title_entry.delete(0, END)
        title_entry.insert(END, selected_tupule[1])
        
        author_entry.delete(0, END)
        author_entry.insert(END, selected_tupule[2])
        
        year_entry.delete(0, END)
        year_entry.insert(END, selected_tupule[3])
        
        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_tupule[4])
    except IndexError:
        pass

def viewcommand():
    listbox.delete(0, END)
    for row in backend.view_all():
        listbox.insert(END, row)

def searchcommand():
    listbox.delete(0, END)
    for row in backend.search_entry(t.get(), a.get(), y.get(), num.get()):
        listbox.insert(END, row)

def addcommand():
    backend.add_entry(t.get(), a.get(), y.get(), num.get())
    listbox.delete(0, END)
    listbox.insert(END, (t.get(), a.get(), y.get(), num.get()))

def deletecommand():
    backend.delete_entry(selected_tupule[0])

def updatecommand():
    backend.update_entry(selected_tupule[0], t.get(), a.get(), y.get(), num.get())

window = Tk()
window.wm_title("Book Info")

# Button widgets
view_button = Button(window, text= "View all", command= viewcommand, width= 12)
view_button.grid(row= 2, column= 3)

search_button = Button(window, text="Search entry", command= searchcommand, width= 12)
search_button.grid(row= 3, column= 3)

add_button = Button(window, text= "Add entry", command= addcommand, width= 12)
add_button.grid(row= 4, column= 3)

update_button = Button(window, text= "Update", command= updatecommand, width= 12)
update_button.grid(row= 5, column= 3)

delete_button = Button(window, text= "Delete", command= deletecommand, width= 12)
delete_button.grid(row= 6, column= 3)

close_button = Button(window, text= "Close", width= 12, command= window.destroy)
close_button.grid(row= 7,column= 3)

# Entry labels
title_label = Label(window, text= "Title")
title_label.grid(row= 0, column= 0)

year_label = Label(window, text= "Year")
year_label.grid(row= 1, column= 0)

author_label = Label(window, text= "Author")
author_label.grid(row= 0, column= 2)

isbn_label = Label(window, text= "ISBN")
isbn_label.grid(row= 1, column= 2)

# Entry widgets
t = StringVar()
title_entry = Entry(window, textvariable= t, width= 20)
title_entry.grid(row= 0, column= 1)

y = StringVar()
year_entry = Entry(window, textvariable= y, width= 20)
year_entry.grid(row= 1, column= 1)

a = StringVar()
author_entry = Entry(window, textvariable= a, width= 20)
author_entry.grid(row= 0, column= 3)

num = StringVar()
isbn_entry = Entry(window, textvariable= num, width= 20)
isbn_entry.grid(row= 1, column= 3)

# Scrollbar and listbox
scroll = Scrollbar(window)
scroll.grid(column= 2, row= 2, rowspan= 5)
listbox = Listbox(window, width= 28, yscrollcommand= scroll.set)
listbox.grid(row= 2, column= 0, rowspan= 6, columnspan= 2, pady= 20, padx= 20)
scroll.config(command=listbox.yview)
listbox.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()