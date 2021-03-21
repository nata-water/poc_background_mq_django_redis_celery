# Generated by Django 3.1.7 on 2021-03-21 11:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('xxx_api', '0004_del_parse_result_column_mq_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='binaryresource',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='binaryresource',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='parseresult',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='parseresult',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='binaryresource',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5013dc92-159e-465d-97f7-b3ba6145e391'), editable=False, primary_key=True, serialize=False),
        ),
    ]