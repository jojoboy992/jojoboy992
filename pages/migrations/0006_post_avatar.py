# Generated by Django 4.2.6 on 2023-10-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avatar',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]
