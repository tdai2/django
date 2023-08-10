# Generated by Django 4.2.4.dev20230807083818 on 2023-08-10 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=25)),
                ('girls_detail', models.JSONField(blank=True)),
                ('ssrs_detail', models.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('type', models.CharField(choices=[('POW', 'POW'), ('TEC', 'TEC'), ('STM', 'STM')], max_length=7)),
                ('birthday', models.DateField()),
                ('pow', models.IntegerField()),
                ('tec', models.IntegerField()),
                ('stm', models.IntegerField()),
                ('apl', models.IntegerField()),
                ('acc_head', models.CharField(max_length=3)),
                ('acc_face', models.CharField(max_length=3)),
                ('acc_hand', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('effect', models.CharField(max_length=50)),
                ('skill_type', models.CharField(choices=[('A', 'A'), ('P', 'P'), ('F', 'F')], max_length=1)),
                ('skill_property', models.CharField(choices=[('POW', 'POW'), ('TEC', 'TEC'), ('STM', 'STM'), ('APL', 'APL'), ('SP', 'SP')], max_length=3)),
                ('pp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ssr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('type', models.CharField(choices=[('POW', 'POW'), ('TEC', 'TEC'), ('STM', 'STM'), ('APL', 'APL')], max_length=3)),
                ('girl', models.CharField(max_length=20)),
                ('pow', models.IntegerField()),
                ('tec', models.IntegerField()),
                ('stm', models.IntegerField()),
                ('apl', models.IntegerField()),
                ('skill1', models.CharField(max_length=50)),
                ('skill2', models.CharField(max_length=50)),
                ('skill3', models.CharField(blank=True, max_length=50)),
                ('notes', models.CharField(blank=True, max_length=200)),
                ('mod', models.BooleanField(default=False)),
                ('Malfunction', models.BooleanField(default=False)),
            ],
        ),
    ]
