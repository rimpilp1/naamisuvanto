# Generated by Django 2.0.13 on 2020-06-29 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saalistilastot', '0007_auto_20200629_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saalis',
            name='viehe',
            field=models.CharField(default='-', max_length=20),
        ),
    ]
