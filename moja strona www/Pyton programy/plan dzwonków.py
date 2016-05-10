print(" Program pokazuje plan dzwonków podczas lekcji ".center(60,"*"))
print()
godzina=input("Podaj pełną godzinę rozpoczęcia pierwszej lekcji: ")
while not godzina.isdigit():
    if not godzina.isdigit():
        godzina=input("Podaj pełną godzinę rozpoczęcia pierwszej lekcji: ")
        continue
    break
    godzina=int(godzina)
    
minuty=input("Podaj minuty: ")
while not minuty.isdigit():
    if not minuty.isdigit():
        minuty=input("Podaj minuty: ")
        continue
    break
    minuty=int(minuty)
    
print()
print('Podanie "0" jako długość przerwy kończy wprowadzanie przerw!')
print()
num=1                                #pierwsza przerwa
przerwy=[]   
print("Podaj długość przerwy nr ", end="")
print(num, end=" ")
przerwa=input()
    
while przerwa!=0:                    #kolejne przerwy
    if not przerwa.isdigit():
        print("Podaj długość przerwy nr ", end="")
        print(num, end=" ")
        przerwa=input()
        continue
    if int(przerwa)>10080:
        przerwa=int(przerwa)-10080
    if 0>int(przerwa):
        continue
    przerwy.append(int(przerwa))   
    num=num+1
    if int(przerwa)==0:
        przerwy=przerwy[:-1]
        break
    print("Podaj długość przerwy nr ", end="")
    print(num, end=" ")
    przerwa=input()
    continue
print()

print("Dzwonek na lekcję  nr 1:\t",end="")
print(godzina,":",minuty)

lekcjamin=int(minuty)+45                #pierwsza lekcja
godzina1=lekcjamin//60
lekcjagodz=int(godzina)+godzina1
lekcjamin=lekcjamin%60
if lekcjagodz>=24:
    lekcjagodz=lekcjagodz%24
print("Dzwonek na przerwę nr 1:\t",end="")    
print(lekcjagodz,":",lekcjamin)

for i in range(len(przerwy)):                       #kolejne przerwy
    lekcjamin=lekcjamin+przerwy[i]
    godzina1=lekcjamin//60
    lekcjagodz=lekcjagodz+godzina1
    lekcjamin=lekcjamin%60
    if lekcjagodz>=24:
        lekcjagodz=lekcjagodz%24
    nr=i+2
    print("Dzwonek na lekcję  nr "+str(nr)+":\t",end="")
    print(lekcjagodz,":",lekcjamin )

    lekcjamin=lekcjamin+45              #kolejne lekcje
    godzina1=lekcjamin//60
    lekcjagodz=lekcjagodz+godzina1
    lekcjamin=lekcjamin%60
    if lekcjagodz>=24:
        lekcjagodz=lekcjagodz%24
    print("Dzwonek na przerwę nr "+str(nr)+":\t",end="")
    print(lekcjagodz,":",lekcjamin )
    
    

