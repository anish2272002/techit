# Generated by Django 4.0.6 on 2022-11-13 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_galleryitem_url_alter_galleryitem_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryitem',
            name='url',
        ),
    ]
