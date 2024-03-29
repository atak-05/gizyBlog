# Generated by Django 4.1.7 on 2023-02-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('name_lastname', models.CharField(max_length=155)),
                ('message', models.TextField()),
                ('createdAtTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
            },
        ),
    ]
