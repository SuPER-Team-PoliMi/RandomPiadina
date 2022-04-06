def elementExist(list, element):
    for subList in list:
        try:
            subList.index(element)
            return True
        except:
            pass
    return False