class setter:

    def __init__(self):
        self.apellido = None
        self.nombre = "Ricardo"

    @property
    def miapellido(self):
        return self.apellido

    @miapellido.setter
    def miapellido(self, value):
        if self.apellido is None:
            self.apellido = value
        print(self.nombre + " " + self.apellido)

    def print_apellido(self):
        return self.nombre + " " + self.apellido


if __name__ == "__main__":
    propiedades = setter()
    propiedades.miapellido = "Roa"
    propiedades.print_apellido()
