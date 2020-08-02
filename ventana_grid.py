from tkinter import *


b = 600
h = 400
marg=50

window = Tk()
window.title('Visualización de Datos')
w = Canvas(window, width=b, height= h)
w.pack()

#principal horizontal
w.create_line(marg, h-marg, b-marg ,h-marg,fill="black")

#Lineas intermedias
v=1
for i in range(marg+50,h-marg,50):
    w.create_line(marg, h-i, b-marg ,h-i ,fill="black",dash=(4, 4,4))
    w.create_text(marg-20,h-i,text=str(v)+" v")
    v+=1

#principal vertical
w.create_line(marg, marg, marg,h-marg,fill="black")

#lineas intermedias
for i in range(marg+50,b-marg,50):
    w.create_line(i, marg, i,h-marg,fill="black",dash=(4, 4,4))

mainloop()
