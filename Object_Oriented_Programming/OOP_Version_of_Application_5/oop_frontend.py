from tkinter import *
from oop_backend import Database

database = Database("books.db")

class window_function(object):
        def __init__(self, window):

                self.window = window

                self.window.wm_title("Book Info")
                
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
                self.t = StringVar()
                self.title_entry = Entry(window, textvariable= self.t, width= 20)
                self.title_entry.grid(row= 0, column= 1)

                self.y = StringVar()
                self.year_entry = Entry(window, textvariable= self.y, width= 20)
                self.year_entry.grid(row= 1, column= 1)

                self.a = StringVar()
                self.author_entry = Entry(window, textvariable= self.a, width= 20)
                self.author_entry.grid(row= 0, column= 3)

                self.num = StringVar()
                self.isbn_entry = Entry(window, textvariable= self.num, width= 20)
                self.isbn_entry.grid(row= 1, column= 3)

                # Button widgets
                view_button = Button(window, text= "View all", command= self.view_command, width= 12)
                view_button.grid(row= 2, column= 3)

                search_button = Button(window, text="Search entry", command= self.search_command, width= 12)
                search_button.grid(row= 3, column= 3)

                add_button = Button(window, text= "Add entry", command= self.add_command, width= 12)
                add_button.grid(row= 4, column= 3)

                update_button = Button(window, text= "Update", command= self.update_command, width= 12)
                update_button.grid(row= 5, column= 3)

                delete_button = Button(window, text= "Delete", command= self.delete_command, width= 12)
                delete_button.grid(row= 6, column= 3)

                close_button = Button(window, text= "Close", width= 12, command= window.destroy)
                close_button.grid(row= 7,column= 3)

                # Scrollbar and listbox
                scroll = Scrollbar(window)
                scroll.grid(column= 2, row= 2, rowspan= 5)
                self.listbox = Listbox(window, width= 28, yscrollcommand= scroll.set)
                self.listbox.grid(row= 2, column= 0, rowspan= 6, columnspan= 2, pady= 20, padx= 20)
                scroll.config(command=self.listbox.yview)
                self.listbox.bind('<<ListboxSelect>>',self.get_selected_row)

        def get_selected_row(self, event):
                try:
                        index = self.listbox.curselection()[0]
                        self.selected_tupule = self.listbox.get(index)
                        self.title_entry.delete(0, END)
                        self.title_entry.insert(END, self.selected_tupule[1])
                        self.author_entry.delete(0, END)
                        self.author_entry.insert(END, self.selected_tupule[2])        
                        self.year_entry.delete(0, END)
                        self.year_entry.insert(END, self.selected_tupule[3])        
                        self.isbn_entry.delete(0, END)
                        self.isbn_entry.insert(END, self.selected_tupule[4])
                except IndexError:
                        pass

        def view_command(self):
                self.listbox.delete(0, END)
                for row in database.view_all():
                        self.listbox.insert(END, row)

        def search_command(self):
                self.listbox.delete(0, END)
                for row in database.search_entry(self.t.get(), self.a.get(), self.y.get(), self.num.get()):
                        self.listbox.insert(END, row)

        def add_command(self):
                database.add_entry(self.t.get(), self.a.get(), self.y.get(), self.num.get())
                self.listbox.delete(0, END)
                self.listbox.insert(END, (self.t.get(), self.a.get(), self.y.get(), self.num.get()))

        def delete_command(self):
                database.delete_entry(self.selected_tupule[0])

        def update_command(self):
                database.update_entry(self.selected_tupule[0], self.t.get(), self.a.get(), self.y.get(), self.num.get())

window = Tk()
window_function(window)
window.mainloop()