# Generated by Django 4.1 on 2024-03-16 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_dailyattendance_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='teamnamedetail',
            fields=[
                ('teamdetail', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Teamdetail',
            },
        ),
    ]
