################################################################################
# Created By Kyle Krug
# Created on 7/9/2019
# This was created to use as a template for a basic Python GUI
################################################################################
from tkinter import Tk, Toplevel,Button,Menu, Label, PanedWindow,VERTICAL,BOTH, StringVar, OptionMenu
#import Python emailing a file
root = Tk()

#creates a function that will add a new window frame to the screen
def nw():
    nw= Toplevel(root)
    nw.title('New Window')
    nw.geometry('200x200')
    closebtn = Button(nw,text='Close', command = nw.destroy)
    closebtn.pack(side = 'bottom', expand = 1)


#This Block of code creates the root window,   
root.title('Basic GUI')
#adds title 
root.geometry('500x500')
#creates size of root window
button = Button(root, text="New Window", command=lambda:nw())
button.pack(side = 'top', expand = 1)
#adds a button and .pack sets the buttons location
closebtn = Button(root,text='Close', command = root.destroy)
closebtn.pack(side = 'bottom', expand = 1)
#adds a close button to teh window

menu= Menu(root)
root.config(menu=menu)
file= Menu(menu)
edit= Menu(menu)
view = Menu(menu)

file.add_command(label = 'exit', command = root.destroy)
menu.add_cascade(label = 'File', menu = file)

edit.add_command(label = 'Holder')
menu.add_cascade(label = 'Edit', menu = edit)

view.add_command(label = 'Holder')
menu.add_cascade(label = 'Holder')


#panels
#p = PanedWindow(root,orient= VERTICAL)
#p.pack(fill = BOTH, expand = 1)
#labelt = Label(p , text = 'Top')
#labelt.pack(side = 'top')
#labelb = Label( p, text = "Bottom")
#labelb.pack(side = 'bottom')
#labelr = Label( p, text = "Right")
#labelr.pack(side = 'right')
#labell = Label( p, text = "Left")
#labell.pack(side = 'left')


#dropdown menu
#variable = StringVar(root)
#variable.set('one') # default value
#w = OptionMenu(root, variable, 'one', 'two','three')
#w.pack()

root.mainloop()

