class Categorias:
    def __init__(self, categorias):
        self.validar_cantidad_categorias(categorias)
        self.categorias = categorias

    def validar_cantidad_categorias(self, categorias):
        if len(categorias) != 5:
            raise ValueError("Debe haber exactamente 5 categorías.")

    def obtener_categorias(self):
        return self.categorias