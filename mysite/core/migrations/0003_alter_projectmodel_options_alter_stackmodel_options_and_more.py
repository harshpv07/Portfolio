# Generated by Django 4.2.1 on 2023-05-20 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_projectmodel_stackmodel_workmodel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectmodel',
            options={'verbose_name_plural': 'ProjectModel'},
        ),
        migrations.AlterModelOptions(
            name='stackmodel',
            options={'verbose_name_plural': 'Stack_Name'},
        ),
        migrations.AlterModelOptions(
            name='workmodel',
            options={'verbose_name_plural': 'Work Name'},
        ),
    ]