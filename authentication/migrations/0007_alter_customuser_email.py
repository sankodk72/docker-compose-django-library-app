# Generated by Django 4.1 on 2023-10-05 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_customuser_is_staff_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
