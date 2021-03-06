# Generated by Django 3.2.2 on 2021-05-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20210430_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(blank=True, choices=[(True, 'Present'), (False, 'Absent')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='mark',
            name='est',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mst',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mark',
            name='quiz1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mark',
            name='quiz2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
