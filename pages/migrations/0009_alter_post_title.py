# Generated by Django 4.2.6 on 2023-10-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_rename_img_avatar_post_image_alter_student_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
