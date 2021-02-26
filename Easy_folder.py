from tkinter import filedialog
from tkinter import *
import os

root = Tk()
root.geometry("480x480")

def folder_selection():
    global folder_selected
    root.withdraw() #hide main window, show only folder selection widget
    folder_selected = filedialog.askdirectory(initialdir="c:/", title="Select location")
    root.deiconify() #show main window again
    label.configure(text=folder_selected)
    print(folder_selected)

def create_folder():
    folder_name = foldername.get()
    path =  folder_selected + "/" + folder_name

    try:
        if not os.path.exists(folder_name):
            os.makedirs(path)
    except OSError:
        print ('Error: Creating directory. ' +  folder_name)

label = Label(root, text='No filepath selected')
folder_button = Button(root, text='Select folder', command=folder_selection)

label1 = Label(root, text='Folder name')
label1.grid(row=0, column=1, sticky=W)    

foldername = StringVar()
folder_input = Entry(root, textvariable=foldername, bd =5)
folder_input.grid(row=0, column=2, sticky=E) 

label.grid(row=2, column=2, columnspan=7, sticky=W)
folder_button.grid(row=2, column=1, sticky=E)

create_folder_button = Button(root, text='Create folder', command=create_folder)
create_folder_button.grid(row=6, column=1, sticky=W)

root.mainloop()

