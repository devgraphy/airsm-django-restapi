# Generated by Django 3.1.5 on 2021-05-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_delete_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
