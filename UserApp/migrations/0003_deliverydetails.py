# Generated by Django 4.2.3 on 2023-07-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_alter_userinfo_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliverydetails',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('adddress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'deliverydetails',
            },
        ),
    ]
