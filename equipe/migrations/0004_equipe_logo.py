# Generated by Django 3.0.7 on 2020-06-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0003_auto_20200607_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/logos/'),
        ),
    ]
