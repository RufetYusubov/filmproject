from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "contact"

    def __str__(self):
        return self.name + " " + self.surname
    