# Generated by Django 3.2.9 on 2021-11-15 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='details',
            field=models.CharField(default='Some String', max_length=500),
        ),
    ]
