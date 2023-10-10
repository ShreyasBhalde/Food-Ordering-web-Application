# Generated by Django 4.2.1 on 2023-07-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0008_alter_menuitem_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=10)),
                ('balance', models.FloatField(default=20000)),
            ],
            options={
                'db_table': 'Accounts',
            },
        ),
    ]
