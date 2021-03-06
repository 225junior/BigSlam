# Generated by Django 3.0.7 on 2020-06-08 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joueur', '0010_auto_20200608_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Position Joeurs',
                'verbose_name_plural': 'Positions Joueurs',
            },
        ),
        migrations.AlterField(
            model_name='joueur',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Position_du_Joueur', to='joueur.Position'),
        ),
    ]
