# Generated by Django 4.0.6 on 2022-12-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_alter_eventmodel_eventtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='eventType',
            field=models.CharField(choices=[('Hackathon', 'Hackathon'), ('Workshop', 'Workshop'), ('Competition', 'Competition')], default=('Competition', 'Competition'), max_length=256),
        ),
    ]