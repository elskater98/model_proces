# Generated by Django 2.1.7 on 2019-03-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0008_auto_20190303_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='select_theme',
            field=models.CharField(choices=[('NATURE', 'NATURE'), ('URBAN', 'URBAN'), ('OTHER', 'OTHER')], default='OTHER', max_length=20),
        ),
    ]