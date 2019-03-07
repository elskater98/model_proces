# Generated by Django 2.1.7 on 2019-03-07 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name to the snap', max_length=64)),
                ('picture', models.ImageField(default='default.png', upload_to='')),
                ('select_theme', models.CharField(choices=[('NATURE', 'NATURE'), ('URBAN', 'URBAN'), ('OTHER', 'OTHER')], default='OTHER', max_length=16)),
                ('select_resolution', models.CharField(choices=[('HD', '1280×720 píxels'), ('FHD', '1920×1080 pixels'), ('QHD', '2560*1440 pixels'), ('UHD', '3840×2160 pixels')], default='FHD', max_length=4)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
