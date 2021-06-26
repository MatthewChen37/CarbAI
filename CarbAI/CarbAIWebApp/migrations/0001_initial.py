# Generated by Django 3.2.4 on 2021-06-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_consumed', models.CharField(max_length=100)),
                ('driving_time', models.DecimalField(decimal_places=2, max_digits=5)),
                ('at_home', models.BooleanField()),
            ],
        ),
    ]
