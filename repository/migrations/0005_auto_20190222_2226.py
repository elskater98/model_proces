# Generated by Django 2.1.7 on 2019-02-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20190222_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(help_text='Enter a name', max_length=200),
        ),
    ]
