# Generated by Django 4.2.7 on 2023-11-28 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locationApp', '0001_initial'),
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DED',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DEDEducationOfficerTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('is_transferred', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DEDSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryEducationOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locationApp.district')),
                ('education_officer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userApp.educationofficer')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locationApp.region')),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryEducationOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locationApp.district')),
                ('education_officer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userApp.educationofficer')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locationApp.region')),
            ],
        ),
        migrations.CreateModel(
            name='DEDVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_date', models.DateTimeField(auto_now_add=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('ded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.districtexecutivedirector')),
            ],
        ),
    ]
