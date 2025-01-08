from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(unique=True)
    contact_number = models.BigIntegerField(default=None,null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    
    class Meta:
        verbose_name = "users"
        db_table = "user"
    
class Ticket_Model(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    section = models.CharField(max_length=1, choices=(('A','Section A'),('B','Section B')))
    seat = models.IntegerField()
    price_paid = models.IntegerField(default=20)
    from_location = models.CharField(max_length=50,default='London')
    to_location = models.CharField(max_length=50,default='France')


    # def __str__(self):
    #     return f"Ticket_Model #{self.pk} - {self.user} - Section : {self.section} - Seat : {self.seat}"
    class Meta:
        verbose_name = "tickets"
        db_table = "ticket"

