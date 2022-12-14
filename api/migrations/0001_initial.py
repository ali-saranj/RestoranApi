# Generated by Django 4.1.3 on 2022-12-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('restaurantId', models.CharField(max_length=1000)),
                ('comment', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('imageTitleUrls', models.CharField(max_length=1000)),
                ('imageUrls', models.CharField(max_length=1000)),
                ('timeWork', models.CharField(max_length=500)),
                ('latitude', models.FloatField(max_length=100)),
                ('longitude', models.FloatField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guId', models.CharField(max_length=1000)),
                ('any', models.JSONField(max_length=10000)),
                ('status', models.CharField(max_length=1000)),
                ('ip', models.CharField(max_length=1000)),
                ('erorr', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Usera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('family', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('passWord', models.CharField(max_length=50)),
            ],
        ),
    ]
