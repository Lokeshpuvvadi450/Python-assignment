# Generated by Django 3.0.5 on 2021-03-30 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital'),
        ),
    ]
