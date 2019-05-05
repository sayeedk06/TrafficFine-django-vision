from django.db import models
from django.conf import settings
# Create your models here.
class Fine(models.Model):
    """This class creates the table named fine with the amount variable for amount assigned by the police
    and number plate stores the text detected from images of the number plate. Finally policeUsername
    variabe creates relationship between the user table and the fine table by creating a ForeignKey"""
    amount = models.PositiveIntegerField()
    numberPlate = models.CharField(max_length=100)
    policeUsername = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.numberPlate
