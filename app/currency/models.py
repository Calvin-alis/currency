from django.db import models

# было на уроки (хороший пример)
class Rate(models.Model):
    sale  = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)
    type  = models.CharField(max_length=3)


# Домашняя работа
# id устанавливать нам не нужно, django автоматически создаст его с инкриментом и не нулевыми значениями
class ContactUs(models.Model):
    email_form  = models.EmailField() #лучший тип для email, так как есть встроенный валидатор(нам не нужно его писать отдельно)
    subject = models.CharField(max_length=15) #
    message = models.CharField(max_length=300) # TextField тут два варианта, первый лучше так как можно установить ограничение(тут все символы будут считаться)


