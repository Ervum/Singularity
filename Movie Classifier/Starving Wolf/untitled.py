def Menu_1():
        MovieList = dict
        while (True):
            Movie = input("Ingrese una pelicula: \n")
            if (Movie == "ninguna"):
                MovieList = dict(sorted(MovieList.items(), key=itemgetter(1), reverse= True))
                return MovieList
            Puntaje = input("Ingrese puntajes \nejemplo: (1,5,7) \n")
            Puntos = Puntaje.split(",")
            PP = int(Puntos[0])*0.5 + int(Puntos[1])*0.3 + int(Puntos[2])*0.2
            MovieList.update({Movie : PP})
