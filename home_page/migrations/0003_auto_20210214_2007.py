# Generated by Django 3.1.4 on 2021-02-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_auto_20210214_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home_features',
            old_name='photo1',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='home_features',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='home_features',
            name='photo3',
        ),
        migrations.RemoveField(
            model_name='home_features',
            name='photo4',
        ),
        migrations.AddField(
            model_name='home_features',
            name='tittle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
