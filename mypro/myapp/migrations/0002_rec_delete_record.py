# Generated by Django 5.0.6 on 2024-07-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('messaage', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='record',
        ),
    ]
