# Generated by Django 4.2.2 on 2023-08-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_sales_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
