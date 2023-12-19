# Generated by Django 4.2.7 on 2023-12-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferApp', '0004_delete_transferapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applicant_type',
            field=models.CharField(choices=[('teacher', 'Exchange Transfer Application'), ('teacher', 'Direct Transfer Application')], max_length=10),
        ),
    ]