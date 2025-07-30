from django.db import models
from django.utils import timezone

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

class DDSRecord(models.Model):
    date = models.DateField(default=timezone.now) # Дата операции
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True) # Статус записи
    type = models.ForeignKey(Type, on_delete=models.PROTECT) # Тип операции(доход/расход)
    category = models.ForeignKey(Category, on_delete=models.PROTECT) # Категория расходов/доходов
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT) # Подкатегория
    amount = models.DecimalField(max_digits=12, decimal_places=2) # Сумма операции
    comment = models.TextField(blank=True, null=True) # Комментарий

    def __str__(self):
        return f"{self.date} - {self.amount} руб."
