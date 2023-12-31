# Generated by Django 4.2.7 on 2023-12-14 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0005_teacher_course'),
        ('officersApp', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userApp.teacher')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.customuser')),
            ],
        ),
    ]
