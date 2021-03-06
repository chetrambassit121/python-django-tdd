from django.db import models
from django.shortcuts import redirect, render, reverse


class List(models.Model):

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])




class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text














# from django.db import models

# class List(models.Model):
#     pass

# class Item(models.Model):
#     text = models.TextField(default='')
#     list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)