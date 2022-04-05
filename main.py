from functions.randomPiadinaSelector import randomPiadinaSelector
from functions.printTitle import printTitle

printTitle()

if 0:
  selection = input("Select mode\n[1] Random piadina generator\n[2] Vote piadina\n[3] Add piadina to database\n[4] Stats\n-> ")
  print()
  randomPiadinaSelector(selection)

randomPiadinaSelector()

print()
print("Enjoy")


