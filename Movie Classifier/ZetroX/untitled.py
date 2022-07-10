from pprint import pprint 

def sortByReview(e):
  return e['review']


movieList = [{"name": "Morbin time", "review":2}, 
             {"name": "Avengers", "review":5},
             {"name": "Doctor extraño", "review":7}, 
             {"name": "Cosas estrañas", "review":1}]

movieList.sort(reverse=True,key=sortByReview)

pprint(movieList)

# Seleccionar el nombre del 1r elemento
print(f"Nombre de la peli con mayor puntuación: {movieList[0]['name']}")
