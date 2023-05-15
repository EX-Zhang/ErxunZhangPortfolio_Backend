from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(db_column="username",max_length=255,primary_key=True)

    password = models.CharField(db_column="password",max_length=255)

    email = models.CharField(db_column="email",max_length=255)

    admin = models.BooleanField(db_column="admin")

    class Meta:
        managed = False
        db_table = 'user'
