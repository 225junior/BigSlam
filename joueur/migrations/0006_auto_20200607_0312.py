# Generated by Django 3.0.7 on 2020-06-07 03:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0003_auto_20200607_0224'),
        ('joueur', '0005_auto_20200607_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='joueur',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joueur',
            name='date_upd',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='joueur',
            name='equipe',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Equipe', to='equipe.Equipe'),
            preserve_default=False,
        ),
    ]
