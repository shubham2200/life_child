from django.db import models

# Create your models here.

class Raise_user(models.Model):
    name = models.CharField(max_length=30 )
    email = models.EmailField(max_length=30 )
    date = models.DateField(auto_now_add=False)
    number = models.IntegerField(max_length=10)
    cause = models.CharField(max_length=20)
    doc_file = models.FileField(upload_to = 'document/' , blank=True, null=True)
    cause_description = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Donate_fund(models.Model):
    donate_fund = models.ForeignKey(Raise_user , on_delete=models.CASCADE)
    full_name = models.CharField(max_length=35)
    email = models.CharField(max_length=35)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=25)
    name_on_card = models.CharField(max_length=35)
    card_number = models.IntegerField(max_length=16)
    amount = models.IntegerField()
    exp_year = models.IntegerField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return str(self.full_name)

