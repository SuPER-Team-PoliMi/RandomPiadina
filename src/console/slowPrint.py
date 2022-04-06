import time

def slowPrint(stringPrint, pause=0.05, newline=True):
  # pause = 0
  for strChar in stringPrint:
    time.sleep(pause)
    print(strChar, end='', flush=True)
  if newline:
    print()