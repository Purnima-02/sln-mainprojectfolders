# Generated by Django 5.0.7 on 2024-08-18 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsaSLN', '0002_demo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Demo',
        ),
        migrations.RemoveField(
            model_name='dsa_applications',
            name='loan_type',
        ),
    ]