'''
Created on Mar 28, 2019
first stable version April 17 2019

@author: miki
'''



##SYSTEM
import os
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
import xlsxwriter



import PySimpleGUI as sg

##SPECIFIC
import dataset2
import mineral_constants
import test
from MainMenu import Example
#import treeviewMinLabels

'''
https://pypi.org/project/PySimpleGUI/
https://pysimplegui.readthedocs.io/tutorial/
https://opensource.com/article/18/8/pysimplegui
'''


class pyMin:
    version = '3.0'

    def __init__(self):
        self.version


def main():
    # print("pyMin.py path using --> print(os.path.dirname(os.path.realpath(__file__))):\n")
    # print(os.path.dirname(os.path.realpath(__file__)))
    print("\n")
    #print("pyMin.py path using --> print(os.path.dirname(os.path.realpath(sys.argv[0])))\n")
    print(os.path.dirname(os.path.realpath(sys.argv[0])))
    filewd = os.path.dirname(os.path.realpath(sys.argv[0]))

    # =======GUI========================================================
    #


    root = Tk()
    root.geometry("670x520+400+30");
    #root.place(x=0, y=0, relwidth=1, relheight=1)
    root.title("pyMin v.3 - Michele Zucali 2019")
    label_root=Label(root, text="Mineral Formula Calculation \n\n michele.zucali@unimi.it\n\n\n "
                                "The Houston Rockets version - Nov-Dec 2019 \n\n\n\n\n\n\n")
    label_root.pack()

##### MENU
    app = Example()

####


    label_window = Toplevel(root)
    label_window.geometry('370x520');
    display_mineral = Label(label_window, text="Mineral Labels and Oxigens!\n see all allowed labels in \n_labelsMIN.xlsx")
    display_mineral.pack()

    Lb_mineral = Listbox(label_window, height=28)
    for k in sorted(mineral_constants.mineral_oxigens.keys()):
        Lb_mineral.insert(END,(k, mineral_constants.mineral_oxigens[k]))
    Lb_mineral.pack()


    output_display = Toplevel(root)
    output_display.geometry('600x300+1300+30')
    label = Label(output_display, text="Output Terminal")
    label.pack()
    #text = Text(output_display)
    text = scrolledtext.ScrolledText(output_display)
    text.pack()
    text.insert(END, "Ready to RUN\n\n")
    #text.configure(state='disabled')


    root.filename = ''

    def UploadAction(event=None):
        root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select mineral oxides input file",
                                               filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")))
        print('Selected:', root.filename)
        text.insert(END, ('Selected:', root.filename,'\n\n'))
        #return root.filename

        saved = sys.stdout
        fout = open("pyMinCalc.log", 'w')
        sys.stdout = writer(sys.stdout, fout)

        print("main in pyMin development")

        pyPTinst = pyMin()
        print("pyMin version....", format(pyPTinst.version))

        print("LOGFILE for pyMinCalc")
        print("pyMinCalc.log")

        dataset2.dataset(root.filename)

        processedFile = open('pyMinCalc.log', 'r')
        # ttk.Label(Tab4, text=[processedFile.read()]).place(x=0, y=27)
        text1 = processedFile.read()

        #text.insert(END, text1)
        text.insert(END, "\nfinishing\n")
        text.insert(END, "\ntask completed\n")
        text.insert(END, "\nsaved to file _OUT and logfile\n")




        print("finishing")
        print("executed")
        sys.stdout = saved
        fout.close()
        print("\n")



###############BUTTONS
    start_button = Button(root, text="Select the File & Run", command=UploadAction).pack()
    close_button= Button(root, text="Close", command=root.destroy).pack()
    root.mainloop()

##### BACK TO TERMINAL-CONSOLE
    print("LIST OF LABELS and associated OXYDES\n")
    for k, v in mineral_constants.mineral_oxigens.items():
        print(k, v)

    ######## SALVA SU XLSX elenco labels per minerali


    workbookNew = xlsxwriter.Workbook(root.filename + '_labelsMIN.xlsx')
    worksheetNEW = workbookNew.add_worksheet()

    row = 0
    col = 0

    for key, value in mineral_constants.mineral_labels.items():
        row += 1
        worksheetNEW.write(row, col, key)
        #       for item in mineral_constants.mineral_labels[key]:
        worksheetNEW.write(row, col + 1, value)
    #       row += 1

    workbookNew.close()
    ##############


    print("system closing")
    sys.exit(0)




    '''
    TO BE implemented:
    1) cation partitioning
    2) AX export
    3) save each mineral
    4) SD
    5) thermobarometry?
    6) plot
    
    '''


class writer:
    def __init__(self, *writers):
        self.writers = writers

    def write(self, text):
        for w in self.writers:
            w.write(text)


def windowsss():
    # import PySimpleGUI as sg      

    layout = [[sg.Text('Persistent window')],
              [sg.Input(do_not_clear=True)],
              [sg.Button('Read'), sg.Exit()]]

    window = sg.Window('Window that stays open', layout)

    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        print(event, values)

    window.Close()


if __name__ == '__main__':
    main()
