import tkinter as tk
import FlamesProcessor as f
from ImgLabel import *

def loadGIF():
	gif = ImageLabel(root)
	gif.pack()
	gif.load('gifs/{}.gif'.format(flamesProcessor.result[0]))
	gif.place(x=100,y=200)

def removeGIF():
	if(gif):gif.unload()

def processEvent():
	flamesProcessor.process(entry1.get(),entry2.get(),label4,canvas1)
	removeGIF()
	loadGIF()
	

if __name__ == "__main__":
	flamesProcessor = f.FlameProcessor()
	util = f.Utility()
	root= tk.Tk()
	canvas1 = tk.Canvas(root, width = 500, height = 500,  relief = 'raised')
	canvas1.pack()

	label1 = tk.Label(root, text='FLAMES CALCULATOR')
	label1.config(font=('helvetica', 14))
	canvas1.create_window(250, 25, window=label1)

	label2 = tk.Label(root, text='Player 1 Name:')
	label2.config(font=('helvetica', 10))
	canvas1.create_window(120, 100, window=label2)	
	
	label3 = tk.Label(root, text='Player 2 Name:')
	label3.config(font=('helvetica', 10))
	canvas1.create_window(120, 120, window=label3)

	label4 = tk.Label(root,text='')
	label4.config(font=('helvetica', 10))

	entry1 = tk.Entry (root) 
	canvas1.create_window(250, 100, window=entry1)
	
	entry2 = tk.Entry (root) 
	canvas1.create_window(250, 120, window=entry2)
		
	button1 = tk.Button(text='Process', command=processEvent, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
	canvas1.create_window(250, 160, window=button1)
	
	#gif
	gif = None
	
	canvas1.pack()

	
	root.mainloop()