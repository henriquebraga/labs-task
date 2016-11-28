from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField('Name', max_length=150)
    email = models.EmailField('Email', max_length=100)
    department = models.CharField('Department', max_length=40)
    created_at = models.DateTimeField('Created at', auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='employees'
        verbose_name = 'employee'
        ordering = ('name',)