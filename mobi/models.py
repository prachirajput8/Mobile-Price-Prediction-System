from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    battery_power=models.FloatField()
    int_memory=models.FloatField()
    fc=models.FloatField()
    n_cores=models.FloatField()
    ram=models.FloatField()
    talk_time=models.FloatField()
    dual_sim=models.FloatField()
    wifi=models.FloatField()
    pc=models.FloatField()
    mobile_wt=models.FloatField()
