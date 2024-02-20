# Generated by Django 3.2 on 2024-02-11 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='gametable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_side', models.CharField(default='white', max_length=50)),
                ('owner_online', models.BooleanField(default=False)),
                ('opponent_online', models.BooleanField(default=False)),
                ('fen', models.CharField(blank=True, max_length=92, null=True)),
                ('pgn', models.TextField(blank=True, null=True)),
                ('winner', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Match cratd.,. Waiting for oponet '), (2, 'Match sTARted'), (3, "Match' Endded")], default=1)),
                ('opponent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
