from django.db import models
import datetime



class PsychoMaster(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    own_id = models.CharField(max_length=255, default='default_own_id')

    def __str__(self):
        return self.name



class Method(models.Model):
    method = models.CharField(max_length=255)
    psycho_master = models.ForeignKey(PsychoMaster, on_delete=models.CASCADE, related_name='methods')

    def __str__(self):
        return self.method

# ----------------------Сохраняем сырые данные------------------------

class RawData(models.Model):
    name = models.CharField(max_length=255)
    data = models.DateField(default=datetime.date.today)
    img = models.ImageField(upload_to='raw_images/')
    own_id = models.CharField(max_length=255, default='default_own_id')

    def __str__(self):
        return self.name


class RawMethod(models.Model):
    method = models.CharField(max_length=255)
    psycho_master = models.ForeignKey(RawData, on_delete=models.CASCADE)

    def __str__(self):
        return self.method

