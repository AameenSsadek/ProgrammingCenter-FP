# Generated by Django 2.2.3 on 2019-10-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0027_bootstrapregister_cssregister_htmlregister_jqregister_jsregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='programmers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('third_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(default=0)),
                ('address1', models.CharField(max_length=150)),
                ('address2', models.CharField(max_length=150)),
                ('address3', models.CharField(max_length=150)),
                ('address4', models.CharField(max_length=150)),
                ('front_id_card', models.ImageField(upload_to='')),
                ('back_id_card', models.ImageField(upload_to='')),
            ],
        ),
    ]
