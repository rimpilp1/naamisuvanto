# Generated by Django 2.0.13 on 2020-07-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saalistilastot', '0008_auto_20200629_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saalis',
            name='paino',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='saalis',
            name='pituus',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
