# Generated by Django 4.0.6 on 2022-07-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('empID', models.CharField(max_length=50)),
                ('empName', models.CharField(max_length=50)),
                ('empDesgination', models.CharField(max_length=50)),
                ('empSalary', models.IntegerField()),
            ],
        ),
    ]
