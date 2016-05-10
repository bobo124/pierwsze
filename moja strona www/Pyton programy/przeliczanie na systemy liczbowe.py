print(" Program przelicza liczby dziesiętne na różne systemy liczbowe ".center(70,"*"))
print()
liczba=int(input("Podaj liczbę: "))
print()
podstawalista=[]
podstawa=1
while podstawa!=0:
    podstawa=int(input("Podaj podstawę systemu: "))
    if podstawa==0:
        break
    podstawalista.append(podstawa)
#print(podstawalista)
print()
l=liczba
lista=[]
for podstawa in podstawalista:
    print()
    liczba=l
    while liczba>0:     #zamiana liczby dziesiętnej
        reszta=liczba%podstawa
        liczba=liczba//podstawa
        lista.append(reszta)
        if liczba==0:
            reszta=liczba
    j=1
    wynik=[]
    print("Liczba", l, "w zapisie", podstawa,"- kowym to:\t ",end="")
    for i in lista:
        if i==10:
            i="A"
        if i==11:
            i="B"
        if i==12:
            i="C"
        if i==13:
            i="D"
        if i==14:
            i="E"
        if i==15:
            i="F"
        wynik.insert(-j,i)
    
        j=j+1
    for i in range(len(wynik)):
        print(wynik[i],end=" ")
    print("(",podstawa,")")
    del lista[:]
    
