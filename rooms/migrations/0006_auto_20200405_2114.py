# Generated by Django 2.2.5 on 2020-04-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20200314_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='roob_photos'),
        ),
    ]