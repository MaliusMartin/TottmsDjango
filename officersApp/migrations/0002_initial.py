# Generated by Django 4.2.7 on 2023-11-28 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('officersApp', '0001_initial'),
        ('locationApp', '0001_initial'),
        ('transferApp', '0001_initial'),
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dedverification',
            name='transfer_verification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transferApp.transferverification'),
        ),
        migrations.AddField(
            model_name='dedsubmission',
            name='ded',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.districtexecutivedirector'),
        ),
        migrations.AddField(
            model_name='dedsubmission',
            name='transfer_submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transferApp.transfersubmission'),
        ),
        migrations.AddField(
            model_name='dededucationofficertransfer',
            name='ded',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.districtexecutivedirector'),
        ),
        migrations.AddField(
            model_name='dededucationofficertransfer',
            name='transfer_application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transferApp.transferapplication'),
        ),
        migrations.AddField(
            model_name='ded',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_executive_directors_district', to='locationApp.district'),
        ),
        migrations.AddField(
            model_name='ded',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_executive_directors_region', to='locationApp.region'),
        ),
        migrations.AddField(
            model_name='ded',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userApp.customuser'),
        ),
    ]
