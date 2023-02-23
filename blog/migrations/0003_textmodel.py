# Generated by Django 4.1.7 on 2023-02-23 12:45

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_categorymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='textModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='textImages')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('createdAtTime', models.DateTimeField(auto_now_add=True)),
                ('updatedAtTime', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='text', to='blog.categorymodel')),
            ],
            options={
                'verbose_name': 'text',
                'verbose_name_plural': 'Texts',
                'db_table': 'text',
            },
        ),
    ]
