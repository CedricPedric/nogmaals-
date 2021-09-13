# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 
amount = ""
toPay = int(float(input('Amount to pay: '))* 100) # Geeft aan hoeveel je moest betalen
payed = int(float(input('Payed amount: ')) * 100) #Geeft aan hoevel je hebt betaald
change = payed - toPay # Wissel geld is betaald min moest betalen.

if change > 0: # Als er wissel geld is groter dan 0 is het True
  coinValue = 500 # De waarde van coin is 500
  
  while change > 0 and coinValue > 0: #Terwijl de waarde van de munt 0 is en het wisselgeld 0 is stpot het met de lus
    nrCoins = change // coinValue # Deelt het getal en doet de uitkomts in integer. Het dumpt het getal na de komma of pun
  

    if nrCoins > 0: # Als het aantal munten groter is dan 0 voert het dit stuk uit
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Print uit de nr coins en de coin value
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) 
      amount = amount + " Aantal: " + str(nrCoinsReturned) +" munten van de waarde " + str(coinValue) + " cent " + "\n" # Berekening van het gebruikte muntstukkken.
      change -= nrCoinsReturned * coinValue # Subtracts the value on the right from the value on the left. Then it assigns it to the expression on the left.
# comment on code below: Dit is een checklist als de value 500 gaat die naar 300 dan naar 200 enz. 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # Als er wisselgeld blijft print het progamma hoeveel er over is
  print('Change not returned: ', str(change) + ' cents')
  print(str(amount))
  
else:
  print('done')
  print(str(amount))