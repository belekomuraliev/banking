import datetime
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    citizenship = models.CharField(max_length=30, default='кыргызстан')
    birth_year = models.DateField('date birth')
    work_place = models.CharField(max_length=30)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Клиента"
        verbose_name_plural = "Клиенты"


    def __str__(self):
        return self.name




class Account(models.Model):
    number = models.CharField(max_length=16, null=True, blank=True)
    account_type = models.IntegerField(default=1, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"


    def __str__(self):
        return self.number

class Credit(models.Model):
    sum = models.CharField(max_length=50, verbose_name='Loans', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Кредит"
        verbose_name_plural = "Кредиты"


    def __str__(self):
        return self.sum
