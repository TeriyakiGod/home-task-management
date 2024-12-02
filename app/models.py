from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    is_parent = models.BooleanField(default=False)
    group = models.CharField(max_length=100)
    pin = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class Duty(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'duties'