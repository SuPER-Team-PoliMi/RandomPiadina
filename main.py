from src.randomPiadinaSelector import randomPiadinaSelector
from src.console.printTitle import cleanAndPrintTitle

cleanAndPrintTitle()

if 1:
  selection = input("Select mode\n[1] Random piadina generator\n[2] Vote piadina\n[3] Add piadina to database\n[4] Stats\n-> ")
  print()
  randomPiadinaSelector(selection)
  print()
  print("Enjoy")
  print()
else:
  randomPiadinaSelector()



