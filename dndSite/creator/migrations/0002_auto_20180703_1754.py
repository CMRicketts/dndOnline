# Generated by Django 2.0.7 on 2018-07-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseChrClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas', models.CharField(default='', max_length=9)),
                ('str_add', models.IntegerField(default=0)),
                ('dex_add', models.IntegerField(default=0)),
                ('wis_add', models.IntegerField(default=0)),
                ('int_add', models.IntegerField(default=0)),
                ('cha_add', models.IntegerField(default=0)),
                ('con_add', models.IntegerField(default=0)),
                ('equip', models.CharField(default='', max_length=500)),
                ('hp', models.IntegerField(default=1)),
                ('skills', models.CharField(default='', max_length=500)),
                ('archetype', models.CharField(default='', max_length=20)),
                ('proficiency', models.CharField(default='', max_length=200)),
                ('prof_bonus', models.IntegerField(default=1)),
                ('armor_name', models.CharField(default='', max_length=10)),
                ('armor_ac', models.IntegerField(default=8)),
                ('resistances', models.CharField(default='', max_length=300)),
                ('weapons', models.CharField(default='', max_length=300)),
                ('features', models.CharField(default='', max_length=300)),
                ('saving_throw', models.CharField(default='', max_length=50)),
                ('hit_dice', models.CharField(default='', max_length=6)),
                ('attacks', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(default='', max_length=10)),
                ('str_add', models.IntegerField(default=0)),
                ('dex_add', models.IntegerField(default=0)),
                ('wis_add', models.IntegerField(default=0)),
                ('int_add', models.IntegerField(default=0)),
                ('cha_add', models.IntegerField(default=0)),
                ('con_add', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=18)),
                ('weight', models.IntegerField(default=100)),
                ('height', models.IntegerField(default=65)),
                ('size', models.CharField(default='', max_length=10)),
                ('speed', models.IntegerField(default=30)),
                ('languages', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='alignment',
            field=models.CharField(default='TN', max_length=2),
        ),
        migrations.AddField(
            model_name='character',
            name='bond',
            field=models.CharField(default='No bonds', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='clas',
            field=models.CharField(default='Barbarian', max_length=9),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='flaw',
            field=models.CharField(default='No flaws (perfection)', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.CharField(default='straight', max_length=10),
        ),
        migrations.AddField(
            model_name='character',
            name='ideals',
            field=models.CharField(default='No ideals', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(default='Human', max_length=10),
        ),
        migrations.AddField(
            model_name='character',
            name='sex',
            field=models.CharField(default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='traits',
            field=models.CharField(default='No traits', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='chr_name',
            field=models.CharField(default='No Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='player_name',
            field=models.CharField(default='No Player', max_length=50),
        ),
    ]