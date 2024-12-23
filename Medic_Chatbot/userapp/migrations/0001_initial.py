# Generated by Django 4.2 on 2023-04-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(db_column='Phone Number', max_length=11, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='media/user/')),
            ],
            options={
                'db_table': 'User Details',
            },
        ),
    ]
