# Generated by Django 4.2.7 on 2023-11-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Recipes', '0003_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
