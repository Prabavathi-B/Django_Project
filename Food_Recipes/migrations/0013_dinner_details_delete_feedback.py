# Generated by Django 4.2.7 on 2023-12-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Recipes', '0012_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='dinner_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
