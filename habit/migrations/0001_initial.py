# Generated by Django 4.2.7 on 2023-11-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место')),
                ('time', models.TimeField(verbose_name='Время')),
                ('action', models.TextField(verbose_name='Действие')),
                ('enjoyable', models.BooleanField(verbose_name='Признак приятной привычки')),
                ('frequency', models.IntegerField(default=1, verbose_name='Периодичность (дни)')),
                ('reward', models.CharField(blank=True, max_length=150, null=True, verbose_name='Вознаграждение')),
                ('time_required', models.DateTimeField(verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
