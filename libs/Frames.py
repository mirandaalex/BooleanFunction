from tkinter import *
from PIL import Image, ImageTk
from modifiDisplay import *
from tablewin import *

#esta es otra clase tkinter.Frame a la cual se le pueden agregar labels, textbot, image, and buttons
class SectionN(Frame):
	sbutton=[]
	stextbox=[]
	slabel=[]
	text_string=["|"]
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
		self.stextbox.append(T)
		return T
	#command llama funciones de la libreria modifiDisplay
	def NButton(self,z,text="None",x=0,y=0,action=0):
		if action==0:
			b = Button(self,height=2, width=10, text=text,command=lambda:AddCharA(text,self.text_string,z))
		elif action ==1:
			b = Button(self,height=2, width=10, text=text,command=lambda:DelChar(self.text_string,z))
		elif action ==2:
			b = Button(self,height=2, width=10, text=text,command=lambda:MoveD(self.text_string,z))
		elif action ==3:
			b = Button(self,height=2, width=10, text=text,command=lambda:MoveI(self.text_string,z))
		elif action ==4:
			b = Button(self,height=2, width=10, text=text,command=lambda:AddCharA("*",self.text_string,z))
		elif action ==5:
			b = Button(self,height=2, width=10, text=text,command=lambda:AddCharA("+",self.text_string,z))
		elif action ==6:
			b = Button(self,height=2, width=10, text=text,command=lambda:AddCharA("~",self.text_string,z))		


		b.place(x=x,y=y)
		self.sbutton.append(b)
		return b

	def DoneButton(self,root,z,text="None",x=0,y=0):
		b = Button(self,height=2, width=10, text=text,command=lambda:NewWindow(root))
		b.place(x=x,y=y)
		self.sbutton.append(b)
		return b


	def NLabel(self,textvar="NONE"):
		label=Label(self,height=7, width=45,background="#A4A4A4",text=textvar)
		label.pack()
		self.slabel.append(label)
		return label
