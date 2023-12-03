
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class ImagesUpload(models.Model):
    image_name = models.CharField(max_length=50,default="sample")
    imagetype_choices = (
        ("public","PUBLIC"),
        ("private","PRIVATE"),
        ("animals","ANIMALS"),
        ("flowers","FLOWERS"),

    )
    image_type = models.CharField(max_length=25,
                                  choices=imagetype_choices,
                                  default="public")
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

