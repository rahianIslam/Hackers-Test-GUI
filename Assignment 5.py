from tkinter import *
from tkinter import Text


def Ttest ():

    pass

def Pval ():
    pass

root = Tk()

root.title('GUI for testing Sneetches')
# Group A widgets 
gA = Label(root, text = 'Group A').grid(row=0, column= 0)
GEA=Entry(root,width="20").grid(row = 1, column= 0,padx=10,pady=10,ipady=40)





#Groiup B widgets 
gB = Label(root, text = 'Group B').grid(row=0, column= 1)
GEB=Entry(root).grid(row = 1, column=1,padx=10,pady=10,ipady=40)

#P test result
Ptbutton =Label(root, text= 'P Value:').grid(row=3, column= 0,sticky= W)
ptentry = Entry(root).grid(row=3, column= 1, sticky = W)

testbut = Button(root, text= 't-test', command = Ttest).grid(row=4, column=0, sticky = W )

root.mainloop()
