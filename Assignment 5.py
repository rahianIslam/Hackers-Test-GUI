import tkinter as tk
from sklearn.utils import shuffle
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import os
# used to put the graph into the window
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import pandas as pd
import seaborn as sns


class HistogramFrame(ttk.Frame):

    def __init__(self, parent= None):

        super().__init__(parent)
        self.grid(sticky = tk.N+tk.S+tk.W+tk.E)
        self.fig = Figure(figsize=(5,5),dpi=100)
        self.ax =self.fig.add_subplot(111)
        self.groupa = list()
        self.groupb = list()
        self.gAVals = []
        self.gBVals = []
        self.diflist  = list()
        self.diff = 0

        self.makewidgets()

    def makewidgets(self):

        # buttons
        ttk.Button(self, text = 'T-test', command = self.valcheck).grid(row=4, column=0)

        #labels 
        ttk.Label(self,text = 'Group A').grid(row=0, column= 0)
        ttk.Label(self,text = 'Group B').grid(row=0, column= 1)
        ttk.Label(self, text= 'P Value:').grid(row=3, column= 0, sticky = tk.W)

        # text boxes for group A , B and Pvalue
        self.grpA = tk.Text(self, width = 10, height= 5)
        
        self.grpB = tk.Text(self, width = 10, height= 5)
        
        self.pval = tk.Text(self, width = 10, height= 1)
        



        self.grpA.grid(row=1, column= 0, sticky = tk.N, padx = 5, pady = 5)
        self.grpB.grid(row=1, column= 1, sticky = tk.N, padx = 5, pady = 5)
        self.pval.grid(row=3, column= 0, sticky = tk.E, pady = 5)

        #A tk.Drawing area linked to the Frame and the matplotlib figure 
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(column = 3, row = 1,columnspan=5, sticky = tk.N+tk.S+tk.E+tk.W )
        self.canvas.draw()

        # this resizes the column when dragged. Over here only column 3 resizes            
        self.columnconfigure(3, weight=1)
        # over her the row 1 resizes. r= 1, c= 3 is the plot. And hence the plot resizes
        self.rowconfigure(1, weight=1)

    def valcheck(self):
        #raeding each value from the text box of both the groups and extracting them
        self.groupa = self.grpA.get('1.0',tk.END+'-1c').split()
        self.groupb = self.grpB.get('1.0',tk.END+'-1c').split()
        # self.pValue()

        # if len(self.groupa)!= 0 and len(self.groupb)!= 0:
        #     try:
        #         for i in range(len(self.groupa)):
        #             self.groupa[i] = float(self.groupa[i])
        #         for i in range(len(self.groupb)):
        #             self.groupb[i] = float(self.groupb[i])
        #         self.pValue()
        #     except:
        #         messagebox.showerror(message="Please enter numerical values only" )
        # else:
        #     messagebox.showerror(message="Please enter values in Group A and Group B boxes" )

        if len(self.groupa) == 0 and len(self.groupb) == 0:

            messagebox.showerror('Error','Please enter values in Group A and Group B boxes')
        else:
            try:
                #test = []
            # turning each value into a float to make sure that they are numbers 
                for i in range(len(self.groupa)):
                    #print(self.groupa[i])
                    self.gAVals.append(float(int(self.groupa[i])))
                    print(str(self.gAVals[i])+ 'After')
                    
                for i in range(len(self.groupb)):
                   # print("heree")
                   # print(self.groupb[i])
                    self.gBVals.append(float(int(self.groupb[i])))
                    print(str(self.gBVals[i])+'AAFter')


                

            except:
                messagebox.showerror('Error','Please enter numerical values only')
        
            self.pValue()
            
    def pValue(self):
        df = pd.DataFrame({
            'star':[float(i) for i in list('1'*len(self.groupa))] + [float(i) for i in list('0'*len(self.groupb))],
            'score':self.groupa + self.groupb})


        meanA= df[df.star==1]['score'].mean()
        meanB= df[df.star==0]['score'].mean()
        self.diff = meanA - meanB

        df['label']= df['star']
        simNum = 10000

        for j in range(simNum):
            shuffle(df['label'])
            meanA = df[df.label==1].score.mean()
            meanB = df[df.label==0].score.mean()
            self.diflist.append(meanA-meanB)

            p = sum( i >= self.diff for i in self.diflist)/simNum
            print(p)
            self.pval.insert('1.0',p)

            self.Hist()

        


    def Hist(self):


        self.ax.hist(self.diflist, bins = 50, color = 'blue')
        self.ax.set_xlabel('Difference in score')
        self.ax.set_ylabel('Number')
        self.ax.plot((self.diff, self.diff),(0,700),color = 'red')
        print(self.pval)
        self.ax.annotate('%2.f%%' % (float(self.pval.get('1.0', 'end'+'-1c'))*100),
                    xytext = (15, 350),
                    xy = (6.6,350),
                    multialignment = 'right',
                    va ='center',
                    color= 'red',
                    size = 'large',
                    arrowprops = {'arrowstyle': '<|-',
                                    'lw': 2,
                                    'color' :'red',
                                    'shrinkA': 10 })

        self.canvas.draw()

        toolFrame = ttk.Frame(self)
        toolFrame.grid(column=3,row=3)
        toolbar = NavigationToolbar2Tk(self.canvas, toolFrame)
        toolbar.update()






    # test case 
    # def addval(self):
    #         return self.groupa + self.groupb
            

    



        


# # Group A widgets 
# gA = tk.Label(root, text = 'Group A').grid(row=0, column= 0)
# GEA=tk.Entry(root,width="20").grid(row = 1, column= 0,padx=10,pady=10,ipady=40)


# #Groiup B widgets 
# gB = tk.Label(root, text = 'Group B').grid(row=0, column= 1)
# GEB=tk.Entry(root).grid(row = 1, column=1,padx=10,pady=10,ipady=40)


# #P test result
# Ptbutton =tk.Label(root, text= 'P Value:').grid(row=3, column= 0, sticky = tk.W)
# ptentry = tk.Entry(root,width="10").grid(row=3, column= 0,sticky = tk.E)

# testbut = tk.Button(root, text= 't-test', command = Ttest(3)).grid(row=4, column=0, sticky = tk.W )



root = tk.Tk()
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
HistogramFrame(root)
root.geometry('800x600')
root.title('GUI for testing Sneetches')
root.mainloop()
