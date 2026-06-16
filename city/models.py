from django.db import models

# Create your models here.
class City(models.Model):

    name=models.CharField(max_length=100)

    description=models.TextField()

    famous_for=models.TextField(default="")

    latitude=models.FloatField()
    longitude=models.FloatField()

    state=models.CharField(max_length=100)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    image = models.ImageField(
        upload_to="cities/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


