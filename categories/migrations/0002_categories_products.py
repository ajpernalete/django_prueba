# Generated by Django 3.0.5 on 2020-04-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
