# Generated by Django 2.0.13 on 2020-07-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saalistilastot', '0009_auto_20200701_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='saalis',
            name='laji',
            field=models.CharField(choices=[('Taimen', 'Taimen'), ('Lohi', 'Lohi')], default='Lohi', max_length=10),
        ),
        migrations.AddField(
            model_name='saalis',
            name='vapautettu',
            field=models.BooleanField(default=False),
        ),
    ]