# Generated by Django 2.2.5 on 2021-02-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('review', models.TextField(max_length=140)),
                ('accuracy', models.IntegerField()),
                ('communication', models.IntegerField()),
                ('cleanliness', models.IntegerField()),
                ('location', models.IntegerField()),
                ('check_in', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
