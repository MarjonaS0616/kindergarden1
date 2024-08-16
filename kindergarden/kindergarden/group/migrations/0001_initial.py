# Generated by Django 5.1 on 2024-08-16 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dads_name', models.CharField(max_length=200)),
                ('mothers_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('going', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educated', models.CharField(max_length=200)),
                ('experience', models.IntegerField()),
                ('married', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(choices=[('bolalar', 'bolalar'), ("o'qituvchi", "o'qituvchi")], max_length=200)),
                ('full_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GroupOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reception_day', models.DateTimeField(auto_now_add=True)),
                ('until_when', models.DateField()),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.kid')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.teacher')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.user')),
            ],
        ),
    ]
