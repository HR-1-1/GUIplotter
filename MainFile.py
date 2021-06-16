##############################################################################################
#Title : GUI application to select a file and plot data
#Author Name : Harish 
#Version : 1.2
#Errors to rectify : select_column Function
##############################################################################################



from tkinter import *
from tkinter import filedialog
from tkinter import messagebox  
import pandas as pd
import numpy as np
#from logging import root
import time
import numpy as np
from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)


arr = np.array([[],[]])
df = pd.DataFrame(arr)
flag=0
def plotter(arr):
    fig, ax = plt.subplots()
    xdata,ydata = [], []
    ln, = plt.plot([], [], 'ro')

    def init():
        ax.set_xlim(0,arr.shape[0])
        ax.set_ylim(np.amin(arr,axis=0)[1], np.amax(arr, axis=0)[1])
        return ln,

    def animate(i):
        xdata.append(i*arr[0,0])
        ydata.append(arr[i,1])
        ln.set_data(xdata, ydata)
        return ln,
	
    ani = FuncAnimation(fig, animate,init_func=init,frames=200,interval=20, blit=True)
        
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas,window)
    #toolbar.update()
    #canvas.get_tk_widget().grid(column =0, row=5)

# Function for opening the
# file explorer window
def browseFiles():
	global v
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("csv files",
														"*.csv*"),
													("Excel files",
														"*.xlsx*"),
													("Log file",
														"*.log*")))
	
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	v = filename

def select_column(Event):
	global flag
	if ((len(column_list.curselection()) == 2)and(flag==0)) :
		df1 = df[[column_list.get(0), column_list.get(1)]]
		global arr
		arr = df1.to_numpy()
		flag=1

def showfile():
	global df
	df = pd.read_csv(v)
	print(df)
	column_list.delete(0, END)
	for col_name in df.columns: 
		column_list.insert(END, col_name)
		
window = Tk()
# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
						    text = "File Explorer using Tkinter")

# column List (Listbox) and Scrollbar
column_list = Listbox(window, height=8, width=50, border=0, selectmode = MULTIPLE)
scrollbar = Scrollbar(window)

# Creating the buttons
button_show = Button(window, 
					 text = "Show File",
					 command = showfile)

button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(window,
					text = "Exit",
					command = exit)

btn_plot = Button(window,
				  text = "Please plot",
				  command = plotter(arr))

'''
#Arrange the widgets
label_file_explorer.grid(column = 0, row = 1)
button_explore.grid(column = 0, row = 2)
button_show.grid(column = 1, row =2)
button_select.grid(column = 2, row =2)
button_exit.grid(column = 1,row = 3)
btn_plot.grid(column=2,row=3)
'''
label_file_explorer.pack()
button_explore.pack()
button_show.pack()
button_exit.pack()
btn_plot.pack()


#column_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#scrollbar.grid(row=4, column=3)

column_list.pack()
scrollbar.pack()

# Set scroll to listbox
column_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=column_list.yview)
# Bind select
column_list.bind('<<ListboxSelect>>', select_column)



# Let the window wait for any events
window.mainloop()

