# Generated by Django 4.2.7 on 2023-11-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Recipes', '0008_veg'),
    ]

    operations = [
        migrations.CreateModel(
            name='non_veg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
