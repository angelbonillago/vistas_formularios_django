from django.db import models

# Create your models here.

class Producto(models.Model): #Modelo abstracto
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    peso=models.CharField(max_length=50)

    class Meta:
        abstract=True


class Refrigeradora(Producto):
    temperatura_minima=models.CharField(max_length=50)
    pantalla_inteligente=models.CharField(max_length=50)
    volumen=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+'  '+self.peso+'  '+self.marca

class Laptop(Producto):
    cpu=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+'  '+self.peso+'  '+self.cpu
  
class Prueba(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    peso=models.CharField(max_length=50)
    cpu=models.CharField(max_length=50)

#Solucion de taller
class Libros(models.Model):

    title=models.CharField(max_length=300)
    authors=models.CharField(max_length=300)
    average_rating=models.CharField(max_length=30)
    isbn=models.CharField(max_length=10)
    isbn13=models.CharField(max_length=13)
    language_code=models.CharField(max_length=10)
    num_pages=models.CharField(max_length=50)
    ratings_count=models.IntegerField()
    text_reviews_count=models.CharField(max_length=300)
    publication_date=models.DateField(auto_now=True)
    publisher=models.CharField(max_length=300)



""" 
 {
   "bookID": 1,
   "title": "Harry Potter and the Half-Blood Prince (Harry Potter  #6)",
   "authors": "J.K. Rowling/Mary GrandPré",
   "average_rating": "4.57",
   "isbn": "0439785960",
   "isbn13": "9780439785969",
   "language_code": "eng",
   "num_pages": "652",
   "ratings_count": 2095690,
   "text_reviews_count": 27591,
   "publication_date": "9/16/2006",
   "publisher": "Scholastic Inc."
 }, """

 #Taller de Proxy y Abstracto
class Salon(models.Model):
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()

class Persona(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    idSalon = models.ForeignKey(Salon, on_delete = models.CASCADE)


    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        abstract = True

class Alumno(Persona): 

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['id', 'first_name', 'last_name'], name = 'primary_key_alumno'
            )
        ]

    def full_name(self):
        return self.last_name + ' '+self.first_name


class OrderedAlum(Alumno): # OrderedAlumno es modelo proxy
    class Meta:
        ordering = ["last_name"]
        proxy = True


class Profesor(Persona):

    
    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['id', 'first_name', 'last_name'], name = 'primary_key_profesor'
            )
        ]

