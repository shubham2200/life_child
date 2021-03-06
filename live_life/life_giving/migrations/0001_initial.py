# Generated by Django 4.0.3 on 2022-03-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raise_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('number', models.IntegerField(max_length=10)),
                ('cause', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('doc_file', models.FileField(blank=True, null=True, upload_to='document')),
                ('cause_description', models.CharField(max_length=50)),
            ],
        ),
    ]
