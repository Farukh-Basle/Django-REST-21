
# pip  install  django-multiselectfield

from django.db import models

from multiselectfield  import  MultiSelectField

class Account(models.Model):
    ROLES = (
        ('pet_owner', 'pet_owner'),
        ('pet_shelter','pet_shelter'),
        ('general_users','general_users'),
        ('veterinarian','veterinarian')
    )
    email = models.EmailField(
        unique=True, max_length=254
    )
    password = models.CharField(max_length=254)
    mobile = models.BigIntegerField(unique=True)

    role_type = MultiSelectField(choices=ROLES)

    image = models.ImageField(
        upload_to='users/' , blank=True, null=True
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.email




