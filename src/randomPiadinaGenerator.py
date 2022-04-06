import numpy as np
import time
import os

from src.globalVars.globalVars import listOfIngredients

from src.random.randomGenerator import generateRandomInt
from src.random.randomGenerator import generateUniqueRandomIngredient
from src.console.printTitle import cleanAndPrintTitle
from src.console.slowPrint import slowPrint
from src.utilities.elementExist import elementExist


def randomPiadinaGenerator(piadinaFirstIngredient = -1, piadinaType = [1,2,2,2], nJolly = 2):
  # piadinaType = [8,7,7,6]
  resultArray = []
  resultArrayString = []

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
      
      randIngredient = generateUniqueRandomIngredient(listGroupIngredients, low, high, size)

      # JOLLY SECTION
      jollyFlag = True
      while jollyFlag == True:  
        if nJolly > 0:
          print(listOfIngredients[iGroup - 1][randIngredient], end='')
          # print(iGroup, randIngredient, listOfIngredients[iGroup - 1][randIngredient], end='')
          jollyStr = input("\t->\t(J)olly? ")
          if jollyStr.lower() == "j":
            nJolly = nJolly - 1
            # print(nJolly, "jolly left")
            randIngredient = generateUniqueRandomIngredient(listGroupIngredients, low, high, size)

            # print(iGroup, randIngredient, listOfIngredients[iGroup - 1][randIngredient])
            print(listOfIngredients[iGroup - 1][randIngredient])
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
  # print(resultArrayString)
  # print()
  # print()
  # print()
  #print(resultArray, sep="\n")
  cleanAndPrintTitle()
  slowPrint("                   ",0.02,newline=False)
  slowPrint("FINAL PIADINA",0.08,newline=False)
  slowPrint("                    ",0.02)
  time.sleep(0.5)
  slowPrint("⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻", 0.02)
  for iGroup in range(0,nGroups):
    # time.sleep(1 * np.abs(np.log(5/(iGroup+1))))
    time.sleep(1 + nGroups * iGroup / 12)
    for iItem in range(0, piadinaType[iGroup]):
      if iItem != piadinaType[iGroup] - 1:
        slowPrint(resultArrayString[iGroup][iItem].ljust(20), 0.03, newline=False)
        slowPrint("\t", newline=False)
      else:
        slowPrint(resultArrayString[iGroup][iItem], 0.03, newline=False)

      time.sleep(1)
    print()
  slowPrint("⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻⁻", 0.02)
  time.sleep(1)

  # Goodbye
  print()
  printPause = 0.01
  if elementExist(resultArrayString,"Senape"):
    slowPrint("Understandable, have a great day!", printPause)
  elif elementExist(resultArrayString,"Patè di olive"):
    slowPrint("LOL", printPause)
  elif elementExist(resultArrayString,"Coppa"):
    slowPrint("Coppa?", printPause)
  elif elementExist(resultArrayString,"Bomba calabra") or elementExist(resultArrayString,"Spianata"):
    if elementExist(resultArrayString,"Bomba calabra") and elementExist(resultArrayString,"Spianata"):
      slowPrint("Extra spicy baby!", printPause)
    slowPrint("Spicy baby!", printPause)
  elif elementExist(resultArrayString,"Tonno"):
    slowPrint("Voulez-vous patè avec moi??", printPause)
  else:
    slowPrint("Enjoy", printPause)
  print()
    
  