# Generated by Django 3.0.5 on 2020-04-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200425_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='delete_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
