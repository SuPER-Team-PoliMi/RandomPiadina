import numpy as np
import random
import time
import os

def generateRandomIngredient(low, high, size=1, seedInt=69):
  rng = np.random.default_rng(random.seed(seedInt))
  randIngredient = rng.integers(low, high, size)
  return int(randIngredient)

def slowPrint(stringPrint, pause=0.05, newline=True):
  # pause = 0
  for strChar in stringPrint:
    time.sleep(pause)
    print(strChar, end='', flush=True)
  if newline:
    print()

def randomPiadinaGenerator(piadinaFirstIngredient = -1, piadinaType = [1,2,2,2]):
  nJolly = 2

  resultArray = []
  resultArrayString = []
  listOfIngredients = [
    ["Crudo", "Salame", "Pancetta", "Cotto", "Bresaola", "Spianata", "Speck", "Coppa"],
    ["Mozzarella", "Grana", "Stracchino", "Edamer", "Scamorza", "Brie", "Formaggio spalmabile"],
    ["Rucola", "Funghi", "Pomodorini", "Zucchine", "lnsalata", "Melanzane", "Tonno"],
    ["Maionese", "Senape", "Salsa rosa", "Salsa boscaiola", "Bomba calabra", "Patè di olive"]
    ]
  nGroups = 4
  
  for iGroup in range(1,nGroups + 1):
    
    low = 0
    size = 1
    if iGroup == 1:
      high = 8
      nIngredients = piadinaType[iGroup - 1]
    elif iGroup == 2:
      high = 7
      nIngredients = piadinaType[iGroup - 1]
    elif iGroup == 3:
      high = 7
      nIngredients = piadinaType[iGroup - 1]
    elif iGroup == 4:
      high = 6
      nIngredients = piadinaType[iGroup - 1]

    listGroupIngredients = []
    listGroupIngredientsString = []

    for iIngredient in range(0,nIngredients):
      listGroupIngredients.append(-1)
      listGroupIngredientsString.append('')
      
      randIngredient = generateRandomIngredient(low, high, size)

      jollyFlag = True
      while jollyFlag == True:

        equalFlag = True
        while equalFlag:
          try:
            listGroupIngredients.index(randIngredient)
            equalFlag = True
            randIngredient = generateRandomIngredient(low, high, size)
          except ValueError:
            equalFlag = False         
                     
          
            
        # JOLLY SECTION
        if nJolly > 0:
          print(iGroup, randIngredient, listOfIngredients[iGroup - 1][randIngredient], end='')
          jollyStr = input("\t->\t(J)olly? ")
          if jollyStr.lower() == "j":
            nJolly = nJolly - 1
            # print(nJolly, "jolly left")
            randIngredient = generateRandomIngredient(low, high, size)
            print(iGroup, randIngredient, listOfIngredients[iGroup - 1][randIngredient])
            jollyFlag = False
          else:
            jollyFlag = False
        else:
          jollyFlag = False
        # end JOLLY SECTION
          
      listGroupIngredients[iIngredient] = randIngredient
      listGroupIngredientsString[iIngredient] = listOfIngredients[iGroup - 1][randIngredient]
      iIngredient = iIngredient + 1
    
    resultArray.append(list(listGroupIngredients))
    resultArrayString.append(list(listGroupIngredientsString))
  
    print()
  print(resultArrayString)
  print()
  print()
  print()
  #print(resultArray, sep="\n")
  os.system('clear')
  slowPrint("                   ",0.02,newline=False)
  slowPrint("FINAL PIADINA",0.08,newline=False)
  slowPrint("                   ",0.02)
  time.sleep(0.5)
  slowPrint("⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻", 0.02)
  for iGroup in range(0,nGroups):
    # time.sleep(1 * np.abs(np.log(5/(iGroup+1))))
    time.sleep(1 + nGroups * iGroup / 12)
    for iItem in range(0, piadinaType[iGroup]):
      slowPrint(resultArrayString[iGroup][iItem], 0.03, newline=False)
      if iItem != piadinaType[iGroup] - 1:
        slowPrint("\t", newline=False)
      time.sleep(1)
    print()
  slowPrint("⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻", 0.02)
  time.sleep(3)
    
  