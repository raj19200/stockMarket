# Generated by Django 3.2.3 on 2021-05-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('contact', models.BigIntegerField()),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]