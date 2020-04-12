import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import os
# used to put the graph into the window
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
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

        self.makewidgets()

    def makewidgets(self):
        # buttons
        ttk.Button(self, text = 'T-test').grid(row=4, column=0 )

        #labels 
        ttk.Label(self,text = 'Group A').grid(row=0, column= 0)
        ttk.Label(self,text = 'Group B').grid(row=0, column= 1)
        ttk.Label(self, text= 'P Value:').grid(row=3, column= 0, sticky = tk.W)

        # text boxes for group A , B and Pvalue
        grpA = tk.Text(self, width = 10, height= 5).grid(row=1, column= 0, sticky = tk.N, padx = 5, pady = 5)
        grpB = tk.Text(self, width = 10, height= 5).grid(row=1, column= 1, sticky = tk.N, padx = 5, pady = 5)
        pval = tk.Text(self, width = 5, height= 1).grid(row=3, column= 0, sticky = tk.E, pady = 5)

        #A tk.Drawing area linked to the Frame and the matplotlib figure 
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(column = 3, row = 1,columnspan=5, sticky = tk.N+tk.S+tk.E+tk.W )
        self.canvas.draw()

        # this resizes the column when dragged. Over here only column 3 resizes            
        self.columnconfigure(3, weight=1)
        # over her the row 1 resizes. r= 1, c= 3 is the plot. And hence the plot resizes
        self.rowconfigure(1, weight=1)

        



        


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
