# Generated by Django 3.2.8 on 2021-11-25 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0015_alter_bingodiscount_unlucky_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='BingoBooster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='BoosterFix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.AlterModelOptions(
            name='lot',
            options={'ordering': ('price',)},
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('bingo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booster_items', to='calculator.bingobooster')),
            ],
        ),
    ]
