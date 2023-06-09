# Generated by Django 4.2.1 on 2023-05-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_name', models.CharField(max_length=100)),
                ('project_date', models.CharField(max_length=100)),
                ('project_descrip', models.CharField(max_length=100)),
                ('proj_related', models.CharField(max_length=100)),
                ('proj_image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stack_name', models.CharField(max_length=100)),
                ('stack_image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100)),
                ('work_image', models.CharField(max_length=100)),
                ('work_role', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'verbose_name_plural': 'ContactModel'},
        ),
    ]
