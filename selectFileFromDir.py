################################################################################
# Created By Kyle Krug
# Created on 7/9/2019
# Created to form a tempate on how to Select a file from the computer Directory
# using a diaolog box
################################################################################
from tkinter.filedialog import askopenfilename, Menu, Tk, Label

root = Tk()

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/",
                           filetypes =(("Python File", "*.py"),("All Files","*.*")),
                           title = "Choose a file.")
    print(name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r', newline = '') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


root.title( "File Opener")
root.geometry('500x500')
label =Label(root, text ="Chose a File!")
label.pack()
#Menu Bar

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = root.destroy)
menu.add_cascade(label = 'File', menu = file)


root.mainloop()
