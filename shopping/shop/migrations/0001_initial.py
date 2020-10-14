# Generated by Django 3.1.1 on 2020-09-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]