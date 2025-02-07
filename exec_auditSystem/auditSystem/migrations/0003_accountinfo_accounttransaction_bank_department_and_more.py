# Generated by Django 4.2.7 on 2023-12-11 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auditSystem', '0002_alter_employeedb_options_alter_statusdb_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('acc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('acc_type', models.CharField(blank=True, max_length=50, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('acc_currency', models.CharField(max_length=10)),
                ('acc_create_date', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'account_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountTransaction',
            fields=[
                ('trans_id', models.IntegerField(primary_key=True, serialize=False)),
                ('trans_type', models.CharField(blank=True, max_length=20, null=True)),
                ('transaction_amount', models.IntegerField()),
                ('trans_currency', models.CharField(max_length=10)),
                ('transaction_status', models.CharField(blank=True, max_length=20, null=True)),
                ('trans_date', models.DateField()),
            ],
            options={
                'db_table': 'account_transaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('bank_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_create_date', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'bank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(blank=True, max_length=50, null=True)),
                ('branch_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentPosition',
            fields=[
                ('position_id', models.IntegerField(primary_key=True, serialize=False)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'department_position',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('degree', models.CharField(blank=True, max_length=20, null=True)),
                ('contract_date', models.DateField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RiskStatus',
            fields=[
                ('status_id', models.IntegerField(primary_key=True, serialize=False)),
                ('st_color', models.CharField(blank=True, max_length=10, null=True)),
                ('st_description', models.CharField(blank=True, max_length=10, null=True)),
                ('risk_p', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'risk_status',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='EmployeeDb',
        ),
        migrations.DeleteModel(
            name='StatusDb',
        ),
        migrations.CreateModel(
            name='EmpNationality',
            fields=[
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auditSystem.employee')),
                ('nationality', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'emp_nationality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Has',
            fields=[
                ('trans', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auditSystem.accounttransaction')),
            ],
            options={
                'db_table': 'has',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalHistory',
            fields=[
                ('emp', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auditSystem.employee')),
                ('history_id', models.IntegerField()),
                ('loan_overdue', models.IntegerField(blank=True, null=True)),
                ('crime_history', models.IntegerField(blank=True, null=True)),
                ('gambling_history', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'personal_history',
                'managed': False,
            },
        ),
    ]
