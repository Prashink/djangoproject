# Generated by Django 4.1.5 on 2023-01-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Brand', models.CharField(max_length=20)),
                ('Model', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Signup1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=9)),
            ],
        ),
    ]
