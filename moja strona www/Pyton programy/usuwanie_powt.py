print(" Program usuwa powtórki sekwencji znaków z napisu ".center(65,"*"))
print()
while True:
    napis=input("Wpisz ciąg znaków max do 100 znaków: ")
    if len(napis)>100 or len(napis)==0:
        print()
        continue
    break
    print()
napisind=[]
for i in range(len(napis)):     #zamiana napisu na listę indeksów
    napisind.append(i)
#print(napisind)                #kontrola
print()
while True:
    wzór=input("Wpisz ciąg znaków do porównania max do 50 znaków: ")
    if len(wzór)>50 or len(wzór)==0:
        print()
        continue
    break
print()
listawzór=[]
listapowt=[]
for i in range(len(napis)):     #określenie początków podciągów w napisie
    el=napis.find(wzór,i)
    #print(napis.find(wzór,i))  #kontrola
    if el not in listawzór and el>=0:
        listawzór.append(el)            
#print(listawzór)               #kontrola
for i in listawzór:             #określenie indeksów do wywalenia z napisów
    for j in range(len(wzór)):
        k=i+j
        if k not in listapowt:
            listapowt.append(k)
#print(listapowt)               #kontrola
napispowywaleniu=[]
for i in napisind:  #wypisanie listy el. napisu pozostałych po usunięciu wzoru
    if i not in listapowt:
        napispowywaleniu.append(i)
#print(napispowywaleniu)        #kontrola
print('Po usunięciu powtórek sekwencji "',wzór,'", pozostaje: ', end="") 
for i in napispowywaleniu:
    print(napis[i], end="")
        
        
