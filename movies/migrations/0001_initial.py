# Generated by Django 3.0.6 on 2020-05-29 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ratings', models.DecimalField(decimal_places=2, max_digits=3)),
                ('genres', models.CharField(max_length=200)),
                ('sentiment', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
