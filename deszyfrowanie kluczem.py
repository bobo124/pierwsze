print(" Program deszyfrujący Kod ENIGMA :) ".center(55,"*"))
print()
napis=input("Podaj słowo: ")
if len(napis)==0:
    while  len(napis)==0:
        print("Słowo musi mieć jakieś litery !!!")
        napis=input("Podaj słowo: ")
        continue
klucz=input("Podaj klucz: ")
if len(klucz)==0:
    while  len(klucz)==0:
        print("Klucz musi mieć jakieś litery !!!")
        klucz=input("Podaj klucz: ")
        continue    
przesunięcielista=[]
napislista=[]
for i in napis:
    napislista.append(ord(i))
#print(napislista)    
for i in klucz:
    if 122>=ord(i)>=97:
        przesunięcie=ord(i)-96
        #print(przesunięcie)
    if 90>=ord(i)>=65:
        przesunięcie=ord(i)-64
        #print(przesunięcie)
    if 48<=ord(i)<=57:
        przesunięcie=ord(i)-48
        
    przesunięcielista.append(przesunięcie)
#print(len(przesunięcielista))
#print(len(napislista))
krotność=len(napislista)/len(przesunięcielista)
if len(napislista)%len(przesunięcielista)!=0:
    krotność=len(napislista)//len(przesunięcielista)+1

if len(napislista)%len(przesunięcielista)==0:
    krotność=len(napislista)//len(przesunięcielista)
#print(krotność)
przesunięcielista=przesunięcielista*krotność
#print(przesunięcielista)
różdługości=len(przesunięcielista)-len(napis)
#print(różdługości)
przesunięcielista=przesunięcielista[:len(przesunięcielista)-różdługości]    
#print("Lista przesunięć: ",przesunięcielista)
nowy=0
kod=0
nowalista=[]
print("Po odszyfrowaniu: ", end="")
for i in range(len(napislista)):
    nowy=napislista[i]-przesunięcielista[i]
    if 97<=napislista[i]<=122:
        if nowy<97:
            nowalista.append(nowy+26)
    
        else:
            nowalista.append(nowy)
    if 65<=napislista[i]<=90:
        if nowy<65:
            nowalista.append(nowy+26)
        else:
            nowalista.append(nowy)
    kod=chr(nowalista[i])
    print(kod, end="")
#print(nowalista)
