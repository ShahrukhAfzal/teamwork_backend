# Generated by Django 3.1.6 on 2021-02-16 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210215_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='project-avatar'),
        ),
    ]