# Generated by Django 3.0.5 on 2020-04-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200425_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='delete_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='delete_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='delete_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='delete_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='delete_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
