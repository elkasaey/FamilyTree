from django.db import models

class Relative(models.Model):
    name = models.CharField(max_length = 80)
    gender = models.CharField(max_length=1,
                              choices=(('M', 'Male'), ('F', 'Female')),
                              blank=False,
                              default=None)
    birthdate = models.DateField(blank=True)
    parents = models.ManyToManyField('self', null=True, blank=True, related_name='children')
