class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def añadir_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"Libros escritos por {self.nombre}:")
        for libro in self.libros:
            print(f"- {libro.titulo}")

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        autor.añadir_libro(self)

autor = Autor("Gabriel García Márquez")
libro1 = Libro("Cien años de soledad", autor)
libro2 = Libro("El amor en los tiempos del cólera", autor)

autor.mostrar_libros()
