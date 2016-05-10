from tkinter import *

#from livewires import games

class Drawing:
    def __init__(self, canvas):
        self.c = canvas
        Widget.bind(self.c, "<Button-1>", self.mouseDown)
        Widget.bind(self.c, "<Button1-Motion>", self.mouseMove)
        

    def mouseDown(self, event):
        self.firstx=self.c.canvasx(event.x)
        self.firsty=self.c.canvasy(event.y)
        

    
okno = Tk()
ramka=Frame(okno)
okno.title(' WIEŻE HANOI')


c=Canvas(okno, width=500, height=300, bg='beige') #Rysowanie wież
c.create_line(110, 150, 110, 250, width=3,fill='brown')
c.create_line(250, 150, 250, 250, width=3,fill='brown')
c.create_line(390, 150, 390, 250, width=3,fill='brown')
c.create_line(70, 250, 150, 250, width=3,fill='brown')
c.create_line(210, 250, 290, 250, width=3,fill='brown')
c.create_line(350, 250, 430, 250, width=3,fill='brown')
info=Label()
info.config(font="SansSerif 14 bold", bg="beige")
info.pack(fill=X)

lista_guzik=[]

lista_w_rece=[]
lista_przycisk=['1','2','3']


lista_wiez=[[1,2,3], [], []]
lista_oval=[[], [], []]

def Rysuj_oval(i, xbegin, towerId): #Funkcja do rysowania ovali
    xstart=xbegin+i*5
    xend=xbegin+80-i*5
    ovals=lista_oval[towerId]
    olen =len(ovals)+1
    ystart=270-olen*20
    yend=270-(olen+1)*20

    ovals.append(c.create_oval(xstart, ystart, xend, yend, width=3,fill='brown'))

for i in range(1,4): #Rysowanie ovali na pierwszej wieży - początek
    Rysuj_oval(i,70,0)

c.pack()

for k in range(1,4): # Utworzenie przycisków
        guzik=Button(ramka,text=lista_przycisk[k-1], bg='grey', width=10,relief=RAISED)
        guzik.config(font="SansSerif 16 bold")
        guzik.grid(row=1,column=k,padx=3)
        ramka.pack()
        
        lista_guzik.append(guzik)


def DoGuzika(wiezaID,xRysuj): #Przenoszenie ovali 
    wieza=lista_wiez[wiezaID]
    if lista_w_rece:
        info.config(fg='beige')
        Rysuj_oval(lista_w_rece[0],xRysuj, wiezaID)
        lista_wiez[wiezaID].append(lista_w_rece[0])
        lista_w_rece.remove(lista_w_rece[0])
        if len(lista_wiez[wiezaID])>=2:
            if lista_wiez[wiezaID][-1]<lista_wiez[wiezaID][-2]:
                info.config(text='Nie wolno kłaść większy krążek na mniejszy!', fg='red')
                lista_w_rece.append(wieza[-1])
                c.delete(lista_oval[wiezaID][-1])
                lista_oval[wiezaID].remove(lista_oval[wiezaID][-1])
                lista_wiez[wiezaID].remove(wieza[-1])              
       
        if lista_wiez[wiezaID]==[1,2,3]:
            info.config(text='Brawo!', fg='yellow green')
    elif lista_w_rece==[]:
        if wieza:
            lista_w_rece.append(wieza[-1])
            c.delete(lista_oval[wiezaID][-1])
            lista_oval[wiezaID].remove(lista_oval[wiezaID][-1])
            lista_wiez[wiezaID].remove(wieza[-1])    
            
def Guzik_1(zd):
    DoGuzika(0,70)
           
def Guzik_2(zd):
    DoGuzika(1,210)
                    
def Guzik_3(zd):
    DoGuzika(2,350)
    
   
lista_guzik[0].bind("<Button-1>", Guzik_1)
lista_guzik[1].bind("<Button-1>", Guzik_2)
lista_guzik[2].bind("<Button-1>", Guzik_3)
        
okno.mainloop()

