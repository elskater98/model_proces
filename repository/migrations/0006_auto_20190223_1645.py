# Generated by Django 2.1.7 on 2019-02-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20190223_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.ImageField(help_text='Choose a picture', upload_to='repository/media/'),
        ),
    ]
