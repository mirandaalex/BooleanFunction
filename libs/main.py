from MainRoot import *
from Frames import *
from tkinter import *
# import time
# time.sleep(5)


root = Tk()
initialFrame=Window(root)

PlaneA=SectionN(root)
PlaneA.Posicion(x=5,y=20)
PlaneA.ColorSet("#A4A4A4")
PlaneA.SetSize(100,330)
#MODIFICA  EL TEXTO EN PANTALLA
z=PlaneA.NLabel()
z.configure(text="HELLO WORD")
z.configure(text="HELLO WORD\nit works!!!!")

#CREA BOTONES
PlaneB=SectionN(root)
PlaneB.Posicion(x=5,y=150)
PlaneB.SetSize(230,330)
PlaneB.ColorSet("#F2F2F2")
PlaneB.NButton("A",25)
PlaneB.NButton("B",125)
PlaneB.NButton("C",225)
PlaneB.NButton("AND \"*\"",25,60)
PlaneB.NButton("OR \"+\"",125,60)
PlaneB.NButton("NOT \"~\"",225,60)
PlaneB.NButton("<- ",25,120)
PlaneB.NButton("->",125,120)
PlaneB.NButton("DEL ",225,120)
#PlaneB.NButton("DEL ",25,180)
#PlaneB.NButton("|",125,180)
PlaneB.NButton("DONE",225,180)


#INICIA VENTANA
root.mainloop()


print("Hola Mundo")