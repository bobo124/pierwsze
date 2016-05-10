from tkinter import *

okno = Tk()
okno.title('Tabliczka mnożenia Canvas')
ramka=Frame(okno)
c=Canvas(okno, width=420, height=420, bg='beige')

m=0
for k in range(0,10):
    c.create_rectangle(10+m, 10, 50+m, 50, fill='green yellow')
    c.create_text(30+m,30,text=k, font="SansSerif 10 bold")
    ramka.pack()
    c.pack()
    m+=40
#c.create_text(30,30,font=" ")
    

n=0
for k in range(0,10):
    c.create_rectangle(10, 10+n, 50, 50+n, fill='green yellow')
    c.create_text(30,30+n,text=k, font="SansSerif 10 bold")
    ramka.pack()
    c.pack()
    n+=40
#c.create_text(30,30,font=" ")
'''
lista=[]
for i in range(1,10):
    podlista=[]
    for j in range(1,10):
        il=i*j
        pole_il=Label(ramka, text=il, bg='lavender')
        pole_il.config(font="SansSerif 16 bold", fg='black')
        pole_il.grid(row=i+1,column=j)
        ramka.pack()
        podlista.append(pole_il)
    lista.append(podlista)
        
 '''
listaZ=[]
for i in range(1,10):
    podlista=[]
    for j in range(1,10):
        il=i*j
        listaZ.append(il)
print(listaZ)
lista_good=[]
for a in range(1,len(listaZ),2):
    
    el=listaZ[a]
    #a+=1
    lista_good.append(el)

print('l',lista_good)
    
l=listaZ
lista=[]         
l=0
x=0
y=0
for i in range(1,10):
    podlista=[]
    k=0
    for j in range(1,10):
        il=i*j
        if il%2==0:
            r='yellow'
            c.create_rectangle(50+k, 50+l, 90+k, 90+l, fill=r)
            c.create_text(70+k,70+l,text=il, font="SansSerif 12 bold")
            k+=40
            ramka.pack()
            c.pack()
            podlista.append(c)
            
        else:               
            r='yellow2'
            c.create_rectangle(50+k, 50+l, 90+k, 90+l, fill=r)
            c.create_text(70+k,70+l,text=il, font="SansSerif 12 bold")
            k+=40
            ramka.pack()
            c.pack()
            podlista.append(c)
           
    lista.append(podlista)
    l+=40

okno.mainloop()
