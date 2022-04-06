import os

from src.globalVars.title import title

from src.console.clearConsole import clearConsole
from src.random.randomGenerator import generateRandomInt


def printTitle(titleIndex):
  print(title[titleIndex])

def cleanAndPrintTitle(titleIndex = 4):
  titleIndex = generateRandomInt(0,len(title),1)
  clearConsole()
  # printTitle(titleIndex)
  printTitle(generateRandomInt(0,len(title),1))
  

