# Generated by Django 3.0.7 on 2020-08-05 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapps', '0012_calendartable_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='clockintable',
            name='group',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dailystatetable',
            name='group',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='leavetable',
            name='group',
            field=models.TextField(blank=True),
        ),
    ]
