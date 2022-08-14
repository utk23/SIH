# Generated by Django 4.0.6 on 2022-08-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_rename_firstname_studata_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studata',
            name='adress1',
        ),
        migrations.RemoveField(
            model_name='studata',
            name='adress2',
        ),
        migrations.RemoveField(
            model_name='studata',
            name='center',
        ),
        migrations.RemoveField(
            model_name='studata',
            name='country',
        ),
        migrations.RemoveField(
            model_name='studata',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='studata',
            name='pincode',
        ),
        migrations.AddField(
            model_name='studata',
            name='nationality',
            field=models.TextField(default='', verbose_name='ntly'),
        ),
        migrations.AlterField(
            model_name='studata',
            name='fullname',
            field=models.TextField(default='', max_length=30, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='studata',
            name='gender',
            field=models.TextField(default='', verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='studata',
            name='password',
            field=models.TextField(default='', verbose_name='fpass'),
        ),
    ]
