# Generated by Django 4.2.1 on 2023-07-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0004_restaurant_image_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='Restaurant_number',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Restaurant_contact_no',
            field=models.IntegerField(default=10, max_length=10),
            preserve_default=False,
        ),
    ]
