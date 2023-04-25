from django.db import models

class Voditels(models.Model):
    fio = models.CharField('fio', max_length=50)
    number_prav = models.CharField('number_prav',unique=True, max_length=15)
    conec_prav = models.DateField('conec_prav')
    primechanie = models.TextField('primechanie')

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return f'/avto/voditels/{self.id}'

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Cars(models.Model):
    marka = models.CharField('marka', max_length=50)
    model = models.CharField('model', max_length=50)
    data_vypuska = models.DateField('data_vypuska')
    vin_number = models.CharField('vin_number',unique=True, max_length=25)
    number_avto = models.CharField('number_avto', max_length=15)
    probeg = models.CharField('probeg', max_length=15)
    voditels = models.OneToOneField(Voditels, on_delete=models.CASCADE)


    def __str__(self):
        return self.marka +' '+ self.number_avto +' '+ self.vin_number

    def get_absolute_url(self):
        return f'/avto/avto/{self.id}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'



class Strahovki(models.Model):
    cars = models.OneToOneField(Cars,on_delete = models.CASCADE)
    sobstvennik_avto = models.CharField('sobstvennik_avto', max_length=50)
    data_nachala = models.DateField('data_nachala')
    data_conca = models.DateField('data_conca')
    number_polisa = models.CharField('number_polisa', unique=True, max_length=15)

    def __str__(self):
        return ""

    def get_absolute_url(self):
        return f'/avto/strahovki/{self.id}'

    class Meta:
        verbose_name = 'Страховка'
        verbose_name_plural = 'Страховки'


class Techosmotr(models.Model):
    cars = models.OneToOneField(Cars,on_delete = models.CASCADE)
    zakazchik = models.CharField('zakazchik', max_length=50)
    data_vydachi = models.DateField('data_vydachi')
    srok_deistviya = models.DateField('srok_deistviya')
    number_tex_karty = models.CharField('number_tex_karty', unique=True, max_length=15)

    def __str__(self):
        return ""

    def get_absolute_url(self):
        return f'/avto/techosmotr/{self.id}'

    class Meta:
        verbose_name = 'Техосмотр'
        verbose_name_plural = 'Техосмотры'