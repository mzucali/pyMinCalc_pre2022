try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


def openfile():

   filename = openfile(parent=root)
   f = open(filename)
   f.read()


root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

tree = Treeview(root)
#
tree["columns"]=("one","two")
tree.column("one", width=100 )
tree.column("two", width=100)
tree.heading("one", text="LABEL")
tree.heading("two", text="OXYGENS")
tree.insert("" , 0,    text="Line 1", values=("1A","1b"))
# ##alternatively:

tree.insert("", 1, "dir4", text="PYROXENE", values=("cpx","6"))
tree.insert("dir4", 6, text="pyroxene",values=("cpx","6"))
tree.insert("dir4", 3, text="px", values=("cpx","6"))
tree.insert("dir4", 4, text="cpx", values=("cpx","6"))
tree.insert("dir4", 5, text="jd", values=("cpx","6"))
tree.insert("dir4", 2, text="augite", values=("cpx","6"))

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
tree.insert("", 1, "dir6", text="FRUITS", values=("fruit","666"))
for k,v in sorted(a_dict.items()):
    tree.insert("dir6", 7, text=k, values=(v, v))


tree.pack()





root.mainloop()


