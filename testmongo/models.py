from django.db import models

# GENDER = {(
#     ('Male': 'Male'),
#     ('Female': 'Female)'
# )
# }

class Cars(models.Model):
    # id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    gender = models.CharField(max_length=6)
    ip_address = models.GenericIPAddressField()
    createdAt = models.TimeField()
    country = models.CharField(max_length=255)
    date = models.DateField()
    car_type = models.CharField(max_length=255)
    manufacture_date = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    


class Name(models.Model):
    name = models.CharField(max_length=255)