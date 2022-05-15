# Generated by Django 3.0.7 on 2020-07-28 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapps', '0007_clockintable_dailystatetable_leavetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='groupAccountTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('account', models.TextField()),
                ('group', models.TextField()),
                ('date', models.DateField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
