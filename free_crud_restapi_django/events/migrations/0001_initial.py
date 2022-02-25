# Generated by Django 3.1.2 on 2022-02-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki Laki'), ('P', 'Perempuan')], default='L', max_length=1)),
                ('nama', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=6)),
                ('other', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
    ]
