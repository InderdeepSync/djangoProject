# Generated by Django 4.0 on 2021-12-10 19:27

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path)),
                ('quantity_available', models.IntegerField(default=0)),
            ],
        ),
    ]