"""
Para hacer que nos de el resultado de una lista de cosas, vamos a seleccionar, en este caso, el lugar que ocupa dicho objeto. 
Por el hecho de que Python usa listas circulares, la posición '-1' siempre será la última de la lista.
"""
def getLastItem(lst):
  return lst[-1]
