# Generated by Django 4.1.6 on 2023-03-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Port', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
