from django.db import models


# было на уроки (хороший пример)
class Rate(models.Model):
    sale  = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)
    type  = models.CharField(max_length=3)

# TODO - усовершествовать типы
# id устанавливать нам не нужно django сам его установит
class ContactUs(models.Model):
    #  установлин автоматический валидатор
    email_form = models.EmailField()
    #  удобно устанавливать ограничения
    subject = models.CharField(max_length=25)
    message = models.TextField()