




class Pagina:



#numero 
#capitolo
#testo

    def __init__(self, numero, capitolo, testo):
        self.numero = numero
        self.capitolo = capitolo
        self.testo = testo

pagina1= Pagina(numero=1, capitolo='Primo Capitolo', testo= 'blah balah')



pagina2= Pagina(numero=2, capitolo='Primo Capitolo', testo='ciap ciop')

print(pagina1.testo)
print(pagina2.testo)

class PaginaSinistra(Pagina):
    def posizione_numero(self):
        return 'sinistra'
        
    pass       

class PaginaDestra(Pagina):
    def posizione_numero(self):
        return 'destra'

libro = []        


pagina3 = PaginaSinistra (numero=1, capitolo='Primo Capitolo', testo= 'blah balah')

libro.append(pagina3)

pagina4 = PaginaDestra (numero=1, capitolo='Primo Capitolo', testo= 'cip e ciop')

libro.append(pagina4)

print(libro)
