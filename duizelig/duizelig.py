a = 30

while a  >= 1:
    print(str(a) + " tot de de lancering begint!")
    a = a - 1 
print("De lancering!")


b = 1

while b <= 24:
    if b >= 0 and b <= 12:
        print(str(b) + " AM")
    else:
        print(str(b) + " PM")
    b = b + 1

c = 20

while c <= 50:
    print(c)
    c = c + 1


day = input("Geef je dag op: ")
if day == "ma":
    d = 1
elif day == 'di':
    d = 2
elif day == 'wo':
    d = 3
elif day == 'do':
    d = 4
elif day == 'vr':
    d = 5
elif day == 'za':
    d = 6
elif day == 'zo':
    d = 7

while d >= 1:
    if d == 1:
        print("Maandag") 
    elif d == 2:
        print("Dinsdag")
    elif d == 3:
        print("Woensdag")
    elif d == 4:
        print("Donderdag")
    elif d == 5:
        print("Vrijdag")
    elif d == 6:
        print("Zaterdag")
    elif d == 7:
        print("Zodag")

    d = d - 1


e = False
f = 1
while e == False:
    print('Dit is poging ' + str(f))
    f = f + 1
    vraagE = input("Vul quit in of niet: ")
    if vraagE == 'quit':
        e = True



teller = 50
som = 0
while som < 1000:  
   som = som + teller
   teller  = teller + 1
   print('Hoevaak' + str(teller))