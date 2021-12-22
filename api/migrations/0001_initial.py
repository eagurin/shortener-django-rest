# Generated by Django 4.0 on 2021-12-22 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=320)),
                ('shorten', models.SlugField(unique=True)),
                ('count', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
                'ordering': ['-pub_date'],
            },
        ),
    ]
