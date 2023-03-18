from django.db import models


class Ingredientes(models.Model):
    nome = models.CharField(max_length=100)
    proteina = models.DecimalField(max_digits=5, decimal_places=2)
    gordura = models.DecimalField(max_digits=5, decimal_places=2)
    carboidrato = models.DecimalField(max_digits=5, decimal_places=2)
    vegetal = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class ItemMedia(models.Model):
    title = models.CharField(max_length=100, default=None)
    imagem = models.ImageField(upload_to='items')

    def __str__(self):
        return self.title


class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tempo_preparacao = models.IntegerField()
    porcao = models.IntegerField()
    alcoolico = models.BooleanField(default=False)
    item_media_id = models.ForeignKey(ItemMedia, on_delete=models.CASCADE, default=None, null=True)
    ingredientes = models.ManyToManyField(Ingredientes, blank=True)

    @property
    def vegano(self):
        if not self.ingredientes.exists():
            return None
        for ingrediente in self.ingredientes.all():
            if ingrediente.vegetal == False:
                return False
        return True

    def __str__(self):
        return self.nome


class MenuMedia(models.Model):
    nome = models.CharField(max_length=100, default=None)
    imagem = models.ImageField(upload_to='menu_image')

    def __str__(self):
        return self.nome


class MenuCategoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

class Menu(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    disponivel = models.BooleanField(default=True)
    categoria = models.ForeignKey(MenuCategoria, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.nome
