# Generated by Django 4.2.1 on 2023-06-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurantadd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant_name', models.CharField(max_length=30)),
                ('Restaurant_city', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Restaurantadd',
            },
        ),
    ]
