# Select randomPiandinaMode
from src.randomPiadinaGenerator import randomPiadinaGenerator
from src.console.printTitle import cleanAndPrintTitle

def randomPiadinaSelector(selector = "1"):
  if selector == "1":
    cleanAndPrintTitle()
    print()
    jollyFlag = input("Do you want jollies? (Y)es/(N)o\n").lower()
    nJollySelected = 2
    if jollyFlag == "n":
      nJollySelected = 0
    cleanAndPrintTitle()
    print("Select ingredients")
    randomPiadinaGenerator(nJolly=nJollySelected)
    