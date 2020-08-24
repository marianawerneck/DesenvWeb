from django.db import models

from categoria.models import Category


class Product(models.Model):

    name = models.CharField(max_length=70, db_index=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    branch = models.CharField(max_length=70, default='')
    slug = models.SlugField(max_length=70)
    image = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    available = models.BooleanField(default=False)

    class Meta:
        db_table="product"
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_availabe(self):
        if self.available:
            return 'Sim'
        else:
            return 'Não'