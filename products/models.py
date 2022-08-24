from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class ActiveCommentManger(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManger, self).get_queryset().filter(active=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)

    # manager
    objects = models.Manager()
    active_comment_manager = ActiveCommentManger()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'good'),
        ('4', 'very good'),
        ('5', 'awesome'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_('Comment Text'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('What is your stars ?'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
