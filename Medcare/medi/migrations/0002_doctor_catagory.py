# Generated by Django 3.1.3 on 2020-12-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='catagory',
            field=models.CharField(choices=[('cardiology', 'cardiology'), ('neorology', 'neorology'), ('nephrology', 'nephrology')], max_length=200, null=True),
        ),
    ]
