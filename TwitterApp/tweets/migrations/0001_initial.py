# Generated by Django 2.2.6 on 2019-10-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=400)),
                ('tag', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=120)),
            ],
        ),
    ]