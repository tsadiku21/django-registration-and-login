# Generated by Django 4.0.6 on 2022-08-20 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_account1_role1_remove_role_accid_delete_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role1',
            name='accId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Student.account1'),
        ),
    ]
