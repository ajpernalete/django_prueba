# Generated by Django 3.0.5 on 2020-04-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/'),
            preserve_default=False,
        ),
    ]
