# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountInfo(models.Model):
    acc_id = models.IntegerField(primary_key=True)
    acc_type = models.CharField(max_length=50, blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    acc_currency = models.CharField(max_length=10)
    acc_create_date = models.CharField(max_length=20, blank=True, null=True)
    emp = models.ForeignKey('Employee', models.DO_NOTHING)
    bank = models.ForeignKey('Bank', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_info'


class AccountTransaction(models.Model):
    trans_id = models.IntegerField(primary_key=True)
    trans_type = models.CharField(max_length=20, blank=True, null=True)
    trans_from = models.ForeignKey(AccountInfo, models.DO_NOTHING, db_column='trans_from', blank=True, null=True)
    trans_to = models.ForeignKey(AccountInfo, models.DO_NOTHING, db_column='trans_to', related_name='accounttransaction_trans_to_set', blank=True, null=True)
    transaction_amount = models.IntegerField()
    trans_currency = models.CharField(max_length=10)
    transaction_status = models.CharField(max_length=20, blank=True, null=True)
    trans_date = models.DateField()
    emp = models.ForeignKey('Employee', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_transaction'


class Bank(models.Model):
    bank_id = models.IntegerField(primary_key=True)
    bank_name = models.CharField(max_length=20, blank=True, null=True)
    bank_create_date = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank'


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=50, blank=True, null=True)
    branch_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DepartmentPosition(models.Model):
    position_id = models.IntegerField(primary_key=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department_position'


class EmpNationality(models.Model):
    emp = models.OneToOneField('Employee', models.DO_NOTHING, primary_key=True)  # The composite primary key (emp_id, nationality) found, that is not supported. The first column is selected.
    nationality = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'emp_nationality'
        unique_together = (('emp', 'nationality'),)


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=20, blank=True, null=True)
    contract_date = models.DateField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING)
    status = models.ForeignKey('RiskStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee'


class Has(models.Model):
    trans = models.OneToOneField(AccountTransaction, models.DO_NOTHING, primary_key=True)  # The composite primary key (trans_id, acc_id) found, that is not supported. The first column is selected.
    acc = models.ForeignKey(AccountInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'has'
        unique_together = (('trans', 'acc'),)


class PersonalHistory(models.Model):
    emp = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)  # The composite primary key (emp_id, history_id) found, that is not supported. The first column is selected.
    history_id = models.IntegerField()
    loan_overdue = models.IntegerField(blank=True, null=True)
    crime_history = models.IntegerField(blank=True, null=True)
    gambling_history = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_history'
        unique_together = (('emp', 'history_id'),)


class RiskStatus(models.Model):
    status_id = models.IntegerField(primary_key=True)
    st_color = models.CharField(max_length=10, blank=True, null=True)
    st_description = models.CharField(max_length=10, blank=True, null=True)
    risk_p = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'risk_status'
