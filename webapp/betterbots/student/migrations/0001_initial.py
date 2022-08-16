# Generated by Django 4.0.6 on 2022-08-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appno', models.TextField(default='', max_length=30, verbose_name='appno')),
                ('username', models.TextField(default='', max_length=10, verbose_name='username')),
                ('fullname', models.TextField(default='', max_length=30, verbose_name='full_name')),
                ('dob', models.DateField(default='2001-1-1', verbose_name='dob')),
                ('email', models.EmailField(default='', max_length=30, verbose_name='email')),
                ('contact', models.TextField(default='', verbose_name='contact')),
                ('gender', models.TextField(default='', verbose_name='gender')),
                ('city', models.TextField(default='', verbose_name='city')),
                ('state', models.TextField(default='', verbose_name='state')),
                ('nationality', models.TextField(default='', verbose_name='ntly')),
                ('answerid', models.TextField(default='', verbose_name='answerid')),
                ('marks', models.TextField(default='', max_length=3, verbose_name='marks')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/STUDENTS PAGE/images/')),
            ],
        ),
    ]
