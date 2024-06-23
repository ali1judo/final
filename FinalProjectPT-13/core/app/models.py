from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=123)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/post_images')
    description = models.TextField()
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
    )
    created_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=13)
    condition = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Новое'),
            (2, 'Б/У')
        )
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'



