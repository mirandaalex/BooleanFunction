from tkinter import *


def NewWindow(root):
	root.iconify()
	Ventana2 = Toplevel(root)
	Ventana2.configure(height=800,width=800)
	Ventana2.resizable(1,1)
	frameAux=Frame(Ventana2,height=800,width=600,bg="#9A2EFE")
	frameAux.pack()
	backbutton=Button(Ventana2,height=2, width=10, text="Back",command=lambda:Switch(root,Ventana2))
	backbutton.pack(side=BOTTOM)
	scrolly=Scrollbar(frameAux)
	scrolly.pack(side=RIGHT,fill=Y)
	listbox=Listbox(frameAux,yscrollcommand=scrolly.set)
	InsertText(listbox)
	listbox.pack()
	scrolly.configure(command=listbox.yview)
	
	if sys.platform.startswith('win32'):
		Ventana2.iconbitmap("..\\image\\cod.ico")
	elif sys.platform.startswith('linux'):
		Ventana2.iconbitmap("../image/cod.ico")
		
def Switch(root,Ventana2):
	root.deiconify()
	Ventana2.destroy()

	
def InsertText(listbox):
	listbox.insert(END, "C   A   B")
	listbox.insert(END, "1   1   1")
	listbox.insert(END, "1   1   0")
	listbox.insert(END, "1   0   1")
	listbox.insert(END, "1   0   0")
	listbox.insert(END, "0   1   1")
	listbox.insert(END, "0   1   0")
	listbox.insert(END, "0   0   1")
	listbox.insert(END, "0   0   0")
