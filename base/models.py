from django.db import models


# Create your models here.
class Gamme(models.Model):
    Nom = models.CharField(max_length=50)
    description = models.CharField(max_length=1000,null=True)
    image = models.ImageField(blank=True,upload_to='gamme/')
    def __str__(self): 
        return  str(self.Nom)

class Categorie(models.Model):
    Nom = models.CharField(max_length=50)
    description = models.CharField(max_length=10000)

    def __str__(self): 
        return str(self.Nom)

class product(models.Model):
    Nom = models.CharField(max_length=50)
    prix = models.FloatField()
    Sell= models.IntegerField()
    nombre_de_stock = models.IntegerField()
    description = models.CharField(max_length=1000, null=True)
    image = models.ImageField(blank=True,upload_to='products/')
    id_Gamme=models.ForeignKey(Gamme,on_delete=models.CASCADE)
    id_Categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)  

    def __str__(self): 
        return self.Nom

class imageP(models.Model):
    image1 = models.ImageField(blank=True,upload_to='products/')
    image2 = models.ImageField(blank=True,upload_to='products/')
    image3 = models.ImageField(blank=True,upload_to='products/')
    id_product=models.ForeignKey(product,on_delete=models.CASCADE)
