from tkinter import *


def Guzik_k_1(zd):
    w=0
    cyfra_k=zd.widget.cget('text')
    polek.config(text=cyfra_k)
    w=int(polek.cget('text'))*int(poler.cget('text'))
    wynik.config(text=w)
    
    if polek.cget('text')==0:
        czynnik_1.config(text=poler.cget('text'))
    czynnik_1.config(text=polek.cget('text'))
    
    ile.focus_set()
    ile.config(text=" ")
    
    

def Guzik_r_1(zd):
        cyfra_r=zd.widget.cget('text')
        poler.config(text=cyfra_r)
        w=int(polek.cget('text'))*int(poler.cget('text'))
        wynik.config(text=w)
        if poler.cget('text')==0:
            czynnik_2.config(text=polek.cget('text'))
        czynnik_2.config(text=poler.cget('text'))
        ile.focus_set()
        ile.config(text=" ")
          

def Wyn(Zd):
    if ile.get().isdigit():
        w=polek.cget('text')*poler.cget('text')
    
        if int(ile.get())==w:
            lista[poler.cget('text')-1][polek.cget('text')-1].config(fg='black')
            ile.config(bg='green yellow')
            puste_1.config(text='BRAWO !',fg='lime green')
        else:
            ile.config(bg='red')
            puste_1.config(text='SPRóBUJ JESZCZE RAZ :(',fg='red')
    else:
        ile.config(bg='red')
        puste_1.config(text='SPRóBUJ JESZCZE RAZ :(',fg='red')
        
def wchodzi(Zdarz):
    Zdarz.widget.config(bg='yellow4')

def schodzi(Zdarz):
    Zdarz.widget.config(bg='yellow2')

def klik(Zdarz):
    Zdarz.widget.config(bg='yellow2')

okno=Tk()

#okno.geometry('500x200')
#ramka=Frame(okno, width=500, height=500)
ramka=Frame(okno, bg='light grey')
okno.title('Tabliczka mnożenia')

lista_k=[]
for k in range(1,10):
    
    pole_k=Button(ramka, text=int(k), width=3, height=1, bg='yellow2')
    pole_k.config(font="SansSerif 16 bold")
    pole_k.grid(row=1,column=k)
    ramka.pack()
    lista_k.append(pole_k)

lista_r=[]
for r in range(1,10):
   
    pole_r=Button(ramka, text=int(r), width=3, height=1, bg='yellow2')
    pole_r.config(font="SansSerif 16 bold")
    pole_r.grid(row=r+1)
    ramka.pack()
    lista_r.append(pole_r)

pole_k.bind_class("Button", "<Enter>", wchodzi)
pole_k.bind_class("Button", "<Leave>", schodzi)
pole_k.bind_class("Button", "<Button-1>", klik)



puste_1=Label(fg='beige')
puste_1.pack(fill=X)
puste_1.config(font="SansSerif 16 bold")


polek=Label(text=0,fg='light grey')
polek.pack(side=LEFT)
polek.config(font="SansSerif 16 bold")

poler=Label(text=0,fg='light grey')
poler.pack(side=LEFT)
poler.config(font="SansSerif 16 bold")

w=int(polek.cget('text'))*int(poler.cget('text'))
wynik=Label(text=w,width=9, height=1,fg='light grey')
wynik.pack(side=LEFT)
wynik.config(font="SansSerif 16 bold")
'''
puste_1=Label(fg='beige')
puste_1.pack(fill=X)
puste_1.config(font="SansSerif 18 bold")
'''

ile_jest=Label(text='Ile jest')
ile_jest.pack(side=LEFT)
ile_jest.config(font="SansSerif 16 bold")

czynnik_1=Label(text=0)
czynnik_1.pack(side=LEFT)
czynnik_1.config(font="SansSerif 16 bold")

iks=Label(text='x')
iks.pack(side=LEFT)
iks.config(font="SansSerif 16 bold")

czynnik_2=Label(text=0)
czynnik_2.pack(side=LEFT)
czynnik_2.config(font="SansSerif 16 bold")

 
puste_2=Label(text='?')
puste_2.pack(side=LEFT)
puste_2.config(font="SansSerif 16 bold")

text=StringVar()
text='?'
ile=Entry(textvariable=text, relief=SUNKEN, width=3, cursor='center_ptr', bg='Grey')
ile.pack(side=LEFT)
ile.config(font="SansSerif 16 bold")
ile.bind("<Return>", Wyn)

kom=Label()
kom.pack(side=RIGHT)
kom.config(font="SansSerif 18 bold")

lista=[]
for i in range(1,10):
    podlista=[]
    for j in range(1,10):
        il=i*j
        pole_il=Label(ramka, relief=SUNKEN, text=il, width=3, height=1, bg='light grey')
        pole_il.config(font="SansSerif 16 bold", fg='light grey')
        pole_il.grid(row=i+1,column=j)
        ramka.pack()
        podlista.append(pole_il)
    lista.append(podlista)


#pole_k.bind_class("Button","<Button-1>", Guzik_k)
for k in lista_k:
    k.bind("<Button-1>", Guzik_k_1)

for r in lista_r:
    r.bind("<Button-1>", Guzik_r_1)

okno.mainloop()
