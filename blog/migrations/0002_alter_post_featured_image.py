# Generated by Django 3.2.16 on 2022-12-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='placeholder', upload_to='media/images/'),
        ),
    ]