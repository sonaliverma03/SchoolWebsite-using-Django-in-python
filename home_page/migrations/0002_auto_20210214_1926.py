# Generated by Django 3.1.4 on 2021-02-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='studentlife',
            options={'ordering': ['-id']},
        ),
    ]
