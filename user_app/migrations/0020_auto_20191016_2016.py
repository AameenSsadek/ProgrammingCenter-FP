# Generated by Django 2.2.3 on 2019-10-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0019_auto_20191016_1534'),
    ]

    operations = [
        migrations.DeleteModel(
            name='html',
        ),
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.EmailField(default='a', max_length=254),
        ),
        migrations.AddField(
            model_name='register',
            name='first_name',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AddField(
            model_name='register',
            name='last_name',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AddField(
            model_name='register',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='register',
            name='second_name',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AddField(
            model_name='register',
            name='third_name',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
