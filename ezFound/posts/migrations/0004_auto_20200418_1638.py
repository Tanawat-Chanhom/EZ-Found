# Generated by Django 3.0.5 on 2020-04-18 16:38

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200418_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[(posts.models.StatusPost['lost'], 'Lost'), (posts.models.StatusPost['found'], 'Found'), (posts.models.StatusPost['returned'], 'Returned')], max_length=10),
        ),
    ]
