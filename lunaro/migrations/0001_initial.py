# Generated by Django 4.0.6 on 2022-08-26 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_a', models.SmallIntegerField()),
                ('score_b', models.SmallIntegerField()),
                ('delta_a', models.SmallIntegerField()),
                ('delta_b', models.SmallIntegerField()),
                ('time', models.DateTimeField(verbose_name='time')),
                ('player_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_a', to='lunaro.player')),
                ('player_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_b', to='lunaro.player')),
            ],
        ),
    ]
