# Generated by Django 4.2.1 on 2023-07-06 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0006_menucategory_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(max_length=12)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.CreateModel(
            name='mycart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.menuitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.userinfo')),
            ],
            options={
                'db_table': 'mycart',
            },
        ),
    ]