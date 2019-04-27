from tkinter import *
from PIL import Image, ImageTk

#esta es otra clase tkinter.Frame a la cual se le pueden agregar labels, textbot, image, and buttons
class SectionN(Frame):
	
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master=master
		self.configure(height=50, width=300,background="#9A2EFE")
		self.place()

	#INSERTA UNA IMAGEN
	def ImageIns(self,x=0,y=0,string="default.png"):
		if sys.platform.startswith('win32'):
			string="..\\image\\"+string
		elif sys.platform.startswith('linux'):
			string="../image/"+string

		load=Image.open(string)
		render=ImageTk.PhotoImage(load)
		img=Label(self,image=render)
		img.image=render
		img.place(x=x,y=y)
	#Cambia la posicion del frame
	def Posicion(self,x=0,y=0):
		self.place(x=x,y=y)

	#Cambia el color del frame
	def ColorSet(self,backgroundd="#9A2EFE"):
		self.configure(background=backgroundd)

	#Cambia el tamaño del frame
	def SetSize(self,x=50,y=300):
		self.configure(height=x,width=y)


	#TEXTBOX BUTTON LABEL
	def NTextBox(self,x=50,y=300):
		T=Text(self,height=x,width=y)
		T.place(x=0,y=0)
		T.insert(END, "Just a text Widget\nin two lines\n")
		return T
	def NButton(self,text="None",x=0,y=0):
		b = Button(self,height=2, width=10, text=text)
		b.place(x=x,y=y)
		return b
	def NLabel(self,textvar="NONE"):
		label=Label(self,height=7, width=45,background="#A4A4A4",text=textvar)
		label.pack()
		return label