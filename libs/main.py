from MainRoot import *
from Frames import *
from tkinter import *
# import time
# time.sleep(5)

a=123456789
root = Tk()
initialFrame=Window(root)

PlaneA=SectionN(root)
PlaneA.Posicion(x=5,y=20)
PlaneA.ColorSet("#A4A4A4")
PlaneA.SetSize(100,330)
#MODIFICA  EL TEXTO EN PANTALLA
z=PlaneA.NLabel()
# z.configure(text="HELLO WORD")
# z.configure(text="HELLO WORD\nit works!!!!")
PlaneA.slabel[0].configure(text="HELLO WORD\nit works!!!!")


#CREA Framework
PlaneB=SectionN(root)
PlaneB.Posicion(x=5,y=150)
PlaneB.SetSize(230,330)
PlaneB.ColorSet("#F2F2F2")
#CREA BOTONES
#parametros 
#1 referencia a label en forma de lista
#2 texto que sale en el boton
#3y4 coordenadas x y
#5 tipo de funcion que hara el boton
PlaneB.NButton([z],"A",25,0,0)
PlaneB.NButton([z],"B",125,0,0)
PlaneB.NButton([z],"C",225,0,0)
PlaneB.NButton([z],"AND \"*\"",25,60,4)
PlaneB.NButton([z],"OR \"+\"",125,60,5)
PlaneB.NButton([z],"NOT \"~\"",225,60,6)
PlaneB.NButton([z],"<- ",25,120,3)
PlaneB.NButton([z],"->",125,120,2)
PlaneB.NButton([z],"DEL ",225,120,1)
PlaneB.NButton([z],"D",25,180,0)
PlaneB.NButton([z],"E",125,180,0)
PlaneB.DoneButton(root,[z],"DONE",225,180)


#INICIA VENTANA
root.mainloop()


print("Hola Mundo")