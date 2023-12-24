# Generated by Django 4.2.7 on 2023-12-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locationApp', '0001_initial'),
        ('userApp', '0005_teacher_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headofschool', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userApp.teacher')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locationApp.school')),
            ],
        ),
    ]