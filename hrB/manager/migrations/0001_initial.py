# Generated by Django 5.0.7 on 2024-11-30 03:50

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import manager.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='custmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='dsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('pan', models.CharField(blank=True, max_length=12, null=True)),
                ('aadhar', models.CharField(max_length=12)),
                ('profession', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('acc_number', models.CharField(max_length=30)),
                ('acc_holder_name', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=30)),
                ('ifsc_code', models.CharField(max_length=40)),
                ('branch_name', models.CharField(max_length=20)),
                ('agreeCheck', models.BooleanField(default=False)),
                ('dsa_registerid', models.CharField(blank=True, max_length=100, null=True)),
                ('dsa_name', models.CharField(blank=True, max_length=100, null=True)),
                ('franchiseCode', models.CharField(max_length=100, null=True)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DSAUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsa_registerid', models.CharField(max_length=100, null=True)),
                ('dsa_name', models.CharField(max_length=100, null=True)),
                ('dsa_password', models.CharField(blank=True, max_length=200, null=True)),
                ('franchiseCode', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='franchise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_id', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('pan', models.CharField(blank=True, max_length=12, null=True)),
                ('aadhar', models.CharField(max_length=12)),
                ('profession', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('agreeCheck', models.BooleanField(default=False)),
                ('dsaPhoto', models.ImageField(upload_to='dsa/', validators=[manager.models.validate_image_file])),
                ('aadharFront', models.ImageField(upload_to='dsa/', validators=[manager.models.validate_image_file])),
                ('aadharBack', models.ImageField(upload_to='dsa/', validators=[manager.models.validate_image_file])),
                ('panCard', models.ImageField(upload_to='dsa/', validators=[manager.models.validate_image_file])),
                ('bankDocument', models.ImageField(upload_to='dsa/', validators=[manager.models.validate_image_file])),
                ('aproval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FranchiseUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HRcredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerid', models.CharField(default='', max_length=100)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('franchiseCode', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('employee_type', models.CharField(choices=[('Backendemployee', 'Loan Process Backend'), ('Accounts', 'Accounts'), ('customersupport', 'Customer Support'), ('sales', 'sales')], max_length=20)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('franchisecode', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='franchisesales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerid', models.CharField(max_length=100, null=True)),
                ('franchiseCode', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('pan', models.CharField(blank=True, max_length=12, null=True)),
                ('aadhar', models.CharField(max_length=12, null=True)),
                ('qualification', models.CharField(max_length=30, null=True)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('Employe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]