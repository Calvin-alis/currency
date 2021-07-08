from django.db import models

# Create your models here.

#id устанавливать нам не нужно django сам его установит
class ContactUs(models.Model):
    email_form = models.EmailField() #  установлин автоматический валидатор
    subject = models.CharField(max_length=25) #  удобно устанавливать ограничения
    message = models.TextField()


