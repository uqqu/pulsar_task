from django.core.validators import FileExtensionValidator
from django.db import models
from PIL import Image


class Products(models.Model):
    statuses = (
        (0, 'В наличии'),
        (1, 'Под заказ'),
        (2, 'Ожидается поступление'),
        (3, 'Нет в наличии'),
        (4, 'Не производится'),
    )

    name = models.CharField('Название', max_length=32)
    part_number = models.CharField('Артикул', max_length=32, unique=True)
    price = models.IntegerField('Цена')
    status = models.IntegerField('Статус', choices=statuses)
    orig_image = models.ImageField(
        'Изображение (jpg/png)',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
    )
    webp_image = models.ImageField()

    def save(self, *args, **kwargs):
        with Image.open(self.orig_image) as img:
            namepath = self.orig_image.path[:-4] + '.webp'
            img.save(namepath, 'webp', quality=95)
            self.webp_image = namepath
        super().save(*args, **kwargs)
