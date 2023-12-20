# Generated by Django 4.2.8 on 2023-12-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADD_EQUIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_AE', models.IntegerField()),
                ('NAME_AE', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ADD_SERV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_AS', models.IntegerField()),
                ('NAME_AS', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='AGREEMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AGREEMENT_ID', models.IntegerField()),
                ('EMPLOYEE_ID', models.IntegerField()),
                ('CLIENT_ID', models.IntegerField()),
                ('DATE', models.DateTimeField()),
                ('ID_COST', models.IntegerField()),
                ('ORGANIZATION_ID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AUTOMOBILE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MODEL', models.CharField(max_length=45)),
                ('AUTOMOBILE_ID', models.IntegerField()),
                ('GENERATION', models.CharField(max_length=45)),
                ('GEAR_BOX', models.CharField(max_length=45)),
                ('DRIVE', models.CharField(max_length=45)),
                ('ENGINE', models.CharField(max_length=45)),
                ('BODY', models.CharField(max_length=45)),
                ('WHEEL', models.CharField(max_length=45)),
                ('ENGINE_POWER', models.IntegerField()),
                ('CAPACITY', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CHECK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_AE', models.IntegerField()),
                ('ID_AS', models.IntegerField()),
                ('AUTOMOBILE_ID', models.IntegerField()),
                ('FIN_COST', models.IntegerField()),
                ('ID_COST', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CLIENTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CLIENT_ID', models.IntegerField()),
                ('FIO_CLIENT', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='EMPLOYEES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMPLOYEE_ID', models.IntegerField()),
                ('JOB_TITLE_ID', models.IntegerField()),
                ('FIO_EMPL', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='JOB_TITLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JOB_TITLE_ID', models.IntegerField()),
                ('SALARY', models.IntegerField()),
                ('NAME', models.CharField(max_length=45)),
                ('DUTY', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ORGANIZATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME_ORG', models.CharField(max_length=30)),
                ('FIO_LEAD', models.CharField(max_length=45)),
                ('PH_NUM', models.CharField(max_length=15)),
                ('ADDRESS', models.CharField(max_length=45)),
                ('ORGANIZATION_ID', models.IntegerField()),
            ],
        ),
    ]
