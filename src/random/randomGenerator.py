import numpy as np
import random

def generateRandomInt(low, high, size=1, seedInt=69):
  rng = np.random.default_rng(random.seed(seedInt))
  randIngredient = rng.integers(low, high, size)
  return int(randIngredient)

def generateUniqueRandomIngredient(listGroupIngredients, low, high, size=1):
  randIngredient = 0
  equalFlag = True
  while equalFlag:
    try:
      listGroupIngredients.index(randIngredient)
      equalFlag = True
      randIngredient = generateRandomInt(low, high, size)
    except ValueError:
      equalFlag = False
  return int(randIngredient)